import threading

class HubApp:
	def __init__(self):
		self.thread = threading.Thread(target = self.test, args = ())

	def test(self):
		pass

	def start(self):
		self.thread.start()

	def run(self):

		return True

	def pause(self):
		self.thread().pause()

		return True

	def stop(self):
		#self.thread().stop()

		return True