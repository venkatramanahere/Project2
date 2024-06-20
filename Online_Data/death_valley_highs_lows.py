from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Online_Data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

"""
for index, column_header in enumerate(header_row):
    print(index, column_header)
""" 
# Plot the high and low temperatures.
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', linewidth = 3, alpha = 0.5)
ax.plot(dates, lows, color='blue', linewidth = 3, alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor='green', alpha = 0.8)

# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize = 20)
ax.set_xlabel('Date of the day', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 10)

plt.show()