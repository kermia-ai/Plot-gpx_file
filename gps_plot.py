import gpxpy
import matplotlib.pyplot as plt

import gpxpy
import folium

# Parse the GPX file
with open("export_1188710.gpx", "r") as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Extract latitudes and longitudes from the GPX data
latitudes = []
longitudes = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            latitudes.append(point.latitude)
            longitudes.append(point.longitude)

# Find the center of the map
center_lat = sum(latitudes) / len(latitudes)
center_lng = sum(longitudes) / len(longitudes)

# Create a folium map
m = folium.Map(location=[center_lat, center_lng], zoom_start=13)

# Add the itinerary as a PolyLine to the map
folium.PolyLine(list(zip(latitudes, longitudes)), color="blue", weight=2.5, opacity=1).add_to(m)

# Save the map as an HTML file
m.save("itinerary_map.html")

# Display the map in a Jupyter Notebook (optional)
# m
