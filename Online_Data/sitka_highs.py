from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Online_Data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)
"""
for index, column_header in enumerate(header_row):
    print(index, column_header)
""" 
# Plot the high temperatures.
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize = 16)
ax.set_xlabel('Date of the day', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 10)

plt.show()