import json

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data.
filename = '../data/eq_data_30_day_m1.json'
with open(filename, encoding="utf-8") as f:
    all_eq_data = json.load(f)

mags, lons, lats, hover_texts = [], [], [], []
for data in all_eq_data['features']:
    if data['properties']['mag'] is not None:
        mags.append(data['properties']['mag'])
        lons.append(data['geometry']['coordinates'][0])
        lats.append(data['geometry']['coordinates'][1])
        hover_texts.append(data['properties']['title'])

# Map the earthquakes.
data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [3 * abs(mag) for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        }
    }]

title = all_eq_data["metadata"]["title"]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')