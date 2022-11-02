import matplotlib.pyplot as plt
from DatabaseManager import DatabaseManager

my_db_mgr = DatabaseManager('../battery_data.db')
db_table = 'battery_data'

rows = None

with my_db_mgr as my_db_mgr_file:
	rows = my_db_mgr_file.conn.execute('select current_datetime, battery_percentage from ' + db_table + '').fetchall()

print(rows)
x_axis, y_axis = [], []

for i in range(len(rows)):
	x_axis.append(rows[i][0])
	y_axis.append(rows[i][1])

plt.plot(x_axis, y_axis)
plt.show()