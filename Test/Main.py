import threading

class HubApp:
	def __init__(self):
		self.thread = threading.Thread(target = self.test, args = ())

	def test(self):
		pass

	def start(self):
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