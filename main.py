import folium
from folium import plugins
import pandas as pd
import requests
from io import BytesIO
import links

# Get data
url = f"https://docs.google.com/spreadsheets/d/{links.sheet_id}/export?gid={links.sheet_name}&format=csv"

df = pd.read_csv(url)

print(df)


# Create a map centered at a specific location
mymap = folium.Map(location=[0, 0], zoom_start=2)

# Add markers for each location
LAT1, LNG1 = 42.3601, 71.0589
LAT2, LNG2 = 37.7749, 122.4194

marker1 = folium.Marker([LAT1, LNG1], popup='Book 1 Location')
marker2 = folium.Marker([LAT2, LNG2], popup='Book 2 Location')

# Connect markers with a line
line = folium.PolyLine(locations=[[LAT1, LNG1], [LAT2, LNG2]], color='red')

# Add markers and line to the map
marker1.add_to(mymap)
marker2.add_to(mymap)
line.add_to(mymap)

# Save the map as an HTML file
mymap.save('book_map.html')