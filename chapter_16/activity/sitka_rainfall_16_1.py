import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '../data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, and high and low temperatures from this file.
    dates, prcps = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            prcp = float(row[3])
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            prcps.append(prcp)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='red', alpha=0.5)
ax.fill_between(dates, prcps, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily precipitation - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (inches)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

plt.show()