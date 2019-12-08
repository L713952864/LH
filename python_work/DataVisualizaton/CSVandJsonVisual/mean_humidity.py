import csv
from matplotlib import pyplot as plt
from datetime import datetime
import pygal

filename = 'sitka_weather_2014.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    head_row = next(reader)
    mean_humidity, dates = [], []
    for row in reader:
        try:
            mean = int(row[8])
            date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print(date, 'Missing data')
        else:
            mean_humidity.append(mean)
            dates.append(date)

hist = pygal.Bar()
hist.title = "Daily mean humidity, - 2014"
hist.x_labels = dates
hist.x_title = 'Date'
hist.y_title = 'Mean Humidity'

hist.add('D6', mean_humidity)
hist.render_to_file('mean_humidity.svg')