import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

# Analising the data structure
filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
fig_title = all_eq_data['metadata']['title']

mags, lats, lons, hover_texts  = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map of earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Bluered',
        'reversescale': False,
        'colorbar': {'title': 'Siła'},
        },
    }]
my_lay = Layout(title=fig_title)

fig={'data': data, 'layout': my_lay}
offline.plot(fig, filename='global_earthquakes.html')