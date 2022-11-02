import json
from pynput import keyboard
from time import localtime, strftime

class HubApp:
	def __init__(self):
		self.listener = keyboard.Listener(on_press = self.on_press)
		self.keys_times_pressed = dict()
		self.paused = False
		self.stopped = False
		self.file_name = 'C:/MyApps/KeyPress/KeyLog/Keys_Pressed_Today_' + self.get_date() + '.txt'

		try:
			self.keys_times_pressed = self.read_from_file()
		except: pass

	def on_press(self, key):
		try:
			k = key.char
		except:
			k = key.name
		
		if not self.paused:
			if k not in self.keys_times_pressed.keys():
				self.keys_times_pressed.update({k:1})
			else:
				self.keys_times_pressed[k] += 1

	def start(self):
		self.listener.start()

	def run(self):
		self.paused = False

		if self.stopped:
			self.__init__()
			self.start()

		return True

	def pause(self):
		self.paused = True
		self.write_to_file()

		return True

	def stop(self):
		self.write_to_file()
		self.listener.stop()
		self.stopped = True

		return True

	def get_date(self):
		return strftime('%y%m%d', localtime())

	def write_to_file(self):
		with open(self.file_name, 'w') as keypress_file:
			keypress_file.write(json.dumps(self.keys_times_pressed))

	def read_from_file(self):
		with open(self.file_name, 'r') as keypress_file:
			file_content = json.loads(keypress_file.read())

		return file_content

	def main(self):
		self.start()
		self.listener.join()

if __name__ == '__main__':
	keypress = HubApp()
	keypress.main()
	
