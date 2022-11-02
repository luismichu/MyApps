import sqlite3, time
from sqlite3 import Error

class DatabaseManager:
	def __init__(self, db_file):
		self.db_file = db_file
		self.__enter__()
		self.create_table()
		self.conn.close()

	def __enter__(self):
		self.conn = None
		try:
			self.conn = sqlite3.connect(self.db_file)
		except Error as e:
			print(e)
		
		return self

	def create_table(self):
		try:
			sql_statement = '''CREATE TABLE IF NOT EXISTS battery_data (
	current_datetime float PRIMARY KEY,
	battery_percentage integer NOT NULL,
	time_remaining integer,
	charging_state integer NOT NULL
);'''

			self.conn.execute(sql_statement)
			self.conn.commit()
		except Error as e:
			print(e)


	def insert(self, table, *values):
		try:
			sql_statement = 'insert into ' + table + ' values(' + ', '.join([str(item) for item in values]) + ');'
			self.conn.execute(sql_statement)
			self.conn.commit()
		except Error as e:
			print(e)

	def select(self, table):
		try:
			sql_statement = 'select * from ' + table
			data = self.conn.execute(sql_statement).fetchall()
		except Error as e:
			print(e)

		return data

	def __exit__(self, type, value, traceback):
		self.conn.close()