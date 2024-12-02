import folium

# Set map center coordinates
map_center = [52.5200, 13.4050]  # Latitude and longitude for Berlin

# Create a folium map object
mymap = folium.Map(location=map_center, zoom_start=15)

# Add a marker to the map
folium.Marker(
    location=[52.5200, 13.4050],  # Latitude and longitude for the marker
    popup="Berlin",               # Popup text
    icon=folium.Icon(color="blue", icon="info-sign")  # Icon settings
).add_to(mymap)

# Display the map
mymap
