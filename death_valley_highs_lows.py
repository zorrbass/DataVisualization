import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    header_dict = {}
    for index, column_header in enumerate(header_row):
        header_dict[index] = column_header
        print(index, column_header)

    # Looping through the heather_dict to get position of TMAX and TMIN

    for index in header_dict:
        if header_dict[index] == "TMIN":
            TMIN_index = index
        if header_dict[index] == "TMAX":
            TMAX_index = index
        if header_dict[index] == "DATE":
            DATE_index = index

    # Get dates and highs and lows from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[DATE_index], "%Y-%m-%d")
        try:
            high = int(row[TMAX_index])
            low = int(row[TMIN_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# print(highs)

# PLot the high and low temperatures
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


# Format plot
title = "Daily high and low temperature - 2018\nDeath Valley ,CA"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()