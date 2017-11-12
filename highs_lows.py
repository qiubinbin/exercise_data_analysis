import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as temp:
	reader = csv.reader(temp)
	header_row = next(reader)
	# for index,column_header in enumerate(header_row):
	# print(index,column_header)
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			low = int(row[3])
			high = int(row[1])
		except ValueError:
			print(date, "missing dates")
		else:  # 成功时执行
			dates.append(date)
			lows.append(low)
			highs.append(high)
	# print(highs)
	# 绘制图形
	fig = plt.figure(dpi=128, figsize=(10, 6))
	plt.plot(dates, highs, c='red', linewidth=0.5)
	plt.plot(dates, lows, c='green', linewidth=0.5)
	plt.fill_between(dates, lows, highs, facecolor='orange', alpha=0.5)
	plt.title("Daily high and low temperatures, July 2014", fontsize=16)
	plt.xlabel('', fontsize=14)
	fig.autofmt_xdate()
	plt.ylabel('Temperature', fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=7)
	plt.savefig('temperature.png')
	plt.show()
