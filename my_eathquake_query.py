import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

import matplotlib.pyplot as plt

filename = "data/tzunami2004.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    header_dict = {}
    for index, column_header in enumerate(header_row):
        header_dict[index] = column_header
        print(index, column_header)

    event_dates = []
    lats = []
    lons = []
    mags = []
    for row in reader:

        event_date = datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S.%fZ")
        lat = row[1]
        lon = row[2]
        mag = float(row[4])
        event_dates.append(event_date)
        lats.append(lat)
        lons.append(lon)
        mags.append(mag)


# Map the earthquakes
# formating dates https://www.youtube.com/watch?v=eirjjyP2qcQ
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": [date.strftime("%A, %d. %B %Y %I:%M%p") for date in event_dates],
    "marker": {
        "size": [mag*mag/2 for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"}
    }
}]


my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
