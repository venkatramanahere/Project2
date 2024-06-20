from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Online_Data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
"""
for index, column_header in enumerate(header_row):
    print(index, column_header)
""" 
# Plot the high temperatures.
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha = 0.5)
ax.plot(dates, lows, color='blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor='green', alpha = 0.8)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize = 16)
ax.set_xlabel('Date of the day', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 10)

plt.show()