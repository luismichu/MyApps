import psutil, sqlite3, time

from sqlite3 import Error

class DatabaseManager():
	def __init__(self, db_file):
		self.db_file = db_file

	def __enter__(self):
		self.conn = None
		try:
			self.conn = sqlite3.connect(self.db_file)
		except Error as e:
			print(e)
		
		return self

	def insert(self, table, *values):
		try:
			sql_statement = 'insert into ' + table + ' values(' + ', '.join([str(item) for item in values]) + ');'
			print(sql_statement)
			self.conn.execute(sql_statement)
			self.conn.commit()
		except Error as e:
			print(e)

	def __exit__(self, type, value, traceback):
		self.conn.close()

def get_battery_data():
	return (psutil.sensors_battery().percent,
			psutil.sensors_battery().secsleft if type(psutil.sensors_battery().secsleft) == int else 0,
			psutil.sensors_battery().power_plugged)


if __name__ == '__main__':	
	my_db_mgr = DatabaseManager('pythonsqlite.db')

	with my_db_mgr as my_db_mgr_file:
		my_db_mgr_file.insert('battery_data', time.time(), *get_battery_data())



