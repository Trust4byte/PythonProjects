import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/eq_data_7_day_m1.json"
with open(filename) as f:
    all_data = json.load(f)

all_data = all_data["features"]

mags, lons, lats, hover_text = [], [], [], []

for eq_dict in all_data:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

data = [{
    "type" : "scattergeo",
    "lon" : lons,
    "lat" : lats,
    "text": hover_text,
    "marker": {
        "size": [5 * mag for mag in mags],
        "color" : mags,
        "colorscale" : "Viridis",
        "reversescale" : True,
        "colorbar" : {"title": "Magnitude"}

}
}]

my_Layout = Layout(title="Global Earthquakes")
fig = {"data" : data, "layout" : my_Layout}
offline.plot(fig, filename="global_earthquakes2.html")