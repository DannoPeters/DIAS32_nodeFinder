import contextily as ctx
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
d = {'name': ['Saskatoon', 'Point1'], 'geometry': [Point(-106.7, 52.1), Point(-109.8, 52.1)]}
gdf = gpd.GeoDataFrame(d, crs="EPSG:25830")
print(gdf)

data_url = "https://ndownloader.figshare.com/files/20232174"
db = gpd.read_file(data_url)
ax = gdf.plot(color="red")
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')
#xlim = ([-170,  170])
#ylim = ([-60,  60])

#ax.set_xlim(xlim)
#ax.set_ylim(ylim)
print(gdf.crs.to_string())
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.CartoDB.Voyager, zoom=18)

plt.show()