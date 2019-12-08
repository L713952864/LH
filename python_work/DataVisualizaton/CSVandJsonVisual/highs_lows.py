import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
filename_valley = 'death_valley_2014.csv'
with open(filename_valley) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    # reader是一个与该文件相关联的阅读器对象，所以得放在with里面
    # 从文件中获取最高气温和日期，已调用过next()所以循环从文件的第二行开始
    # 不能写成列表解析
    valley_dates, valley_highs, valley_lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            valley_highs.append(high)
            valley_dates.append(date)
            valley_lows.append(low)

with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    # reader是一个与该文件相关联的阅读器对象，所以得放在with里面
    # 从文件中获取最高气温和日期，已调用过next()所以循环从文件的第二行开始
    # 不能写成列表解析
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)

# 得知index=0处为日期，index=1处为最高气温
for index, column_header in enumerate(header_row):
    print(index, column_header)

# 设置绘图窗口并绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(valley_dates, valley_highs, c='red', alpha=0.4)
plt.plot(valley_dates, valley_lows, c='blue', alpha=0.4)
plt.plot(dates, highs, c='red', alpha=0.8)
plt.plot(dates, lows, c='blue', alpha=0.8)
# 给图表区域着色
plt.fill_between(valley_dates, valley_highs, valley_lows, facecolor='blue', alpha=0.1)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)
# 设置图形格式
plt.title("Daily high and low temperatures, - 2014", fontsize=20)
plt.xlabel('data', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()