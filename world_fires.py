import csv

from plotly import graph_objects as go


filename = 'data/world_fires_7_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    title_row = next(reader)

    # Just to see indexes of the columns 
    # for i, name in enumerate(title_row):
    #     print(i, name)

    lats, lons, strengths = [], [], []
    for row in reader:
        try:
            lats.append(float(row[0]))
            lons.append(float(row[1]))
            strengths.append(float(row[2]))
        except ValueError:
            print("Data missing")

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [strength for strength in strengths],
        'color': strengths,
        'colorscale': 'Bluered',
        'colorbar': {'title': "Strength"}
        }
    }]

fig = go.Figure(data, layout_title_text="World fires in last 7 days")

fig.write_html('fires.html', auto_open=True)