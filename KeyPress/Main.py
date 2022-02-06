import threading
from pynput import keyboard

class HubApp:
	def __init__(self):
		self.thread = threading.Thread(target = self.main, args = ())
		self.listener = keyboard.Listener(on_press = on_press)

	def on_press(key):
		if key == keyboard.Key.esc:
			return False  # stop listener
		try:
			k = key.char  # single-char keys
		except:
			k = key.name  # other keys
		if k in ['1', '2', 'left', 'right']:  # keys of interest
			# self.keys.append(k)  # store it in global-like variable
			print('Key pressed: ' + k)
			return False  # stop listener; remove this if want more keys


	def start(self):
		self.listener.start()
		self.thread.start()

	def run(self):
		print('run')

		return True

	def pause(self):
		print('pause')

		return True

	def stop(self):
		print('stop')

		return True

	def main(self):

