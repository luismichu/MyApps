import threading

class HubRun:
	def __init__(self):
		self.thread = threading.Thread(target = self.test, args = ())

	def test(self):
		pass

	def start(self):
		self.thread.start()

	def run(self):
		print('test')

		return True

	def pause(self):
		print('test')

		return None

	def stop(self):
		print('test')

		return None