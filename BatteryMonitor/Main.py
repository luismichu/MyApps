import threading, psutil, time
from package.DatabaseManager import DatabaseManager

class HubApp:
	def __init__(self):
		self.thread = threading.Thread(target = self.main, args = ())
		self.paused = False
		self.stopped = False
		self.my_db_mgr = DatabaseManager('battery_data.db')
		self.db_table = 'battery_data'

	def start(self):
		self.thread.start()

	def run(self):

		return True

	def pause(self):
		self.paused = True

		return None

	def stop(self):

		return None

	def get_battery_data(self):
		return (psutil.sensors_battery().percent,
			psutil.sensors_battery().secsleft if type(psutil.sensors_battery().secsleft) == int else 0,
			psutil.sensors_battery().power_plugged)

	def main(self):
		last_battery_percentage = self.get_battery_data()[0]

		while not self.stopped:
			while not self.paused:
				if last_battery_percentage != self.get_battery_data()[0]:

					last_battery_percentage = self.get_battery_data()[0]
					with self.my_db_mgr as my_db_mgr_file:
						my_db_mgr_file.insert(self.db_table, time.time(), *self.get_battery_data())


				time.sleep(5)
			time.sleep(5)


if __name__ == '__main__':
	battery_monitor = HubApp()
	battery_monitor.main()