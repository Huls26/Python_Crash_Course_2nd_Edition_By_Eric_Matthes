import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename, encoding="utf-8") as f:
    all_eq_data = json.load(f)

mags, lons, lats = [], [], []
for data in all_eq_data['features']:
    mag = data['properties']['mag']
    lon = data['geometry']['coordinates'][0]
    lat = data['geometry']['coordinates'][1]
    
    if mag is not None:
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)

# Map the earthquakes.
data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [3 * abs(mag) for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        }
    }]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')