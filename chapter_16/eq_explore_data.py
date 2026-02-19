import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename, encoding="utf-8") as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

mags, lons, lats = [], [], []
for data in all_eq_data['features']:
    mag = data['properties']['mag']
    lon = data['geometry']['coordinates'][0]
    lat = data['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags)
print(all_eq_data)
