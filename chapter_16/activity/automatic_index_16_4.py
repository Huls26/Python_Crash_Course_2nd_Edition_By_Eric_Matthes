import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename1 = '../data/sitka_weather_2018_simple.csv'
filename2 = '../data/death_valley_2018_simple.csv'

def get_high_low(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_obj = {header: idx for idx, header in enumerate(header_row)}

        station_name = None
        # Get dates, and high and low temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            if station_name is None:
                station_name = row[header_obj["NAME"]]

            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[header_obj["TMAX"]])
                low = int(row[header_obj["TMIN"]])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                
        return station_name, dates, highs, lows
    
def plot_temperatures(station_name, dates, highs, lows):
    # matplotlib plotting
    # Plot the high temperatures.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    station_name = station_name.title()
    title = f"Daily high and low temperatures - 2018\n{station_name}"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='minor', labelsize=16)

    plt.show()

station1, dates1, highs1, lows1 = get_high_low(filename1)

station2, dates2, highs2, lows2 = get_high_low(filename2)


plot_temperatures(station1, dates1, highs1, lows1)
plot_temperatures(station2, dates2, highs2, lows2)