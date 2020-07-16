import folium

#Creating the map
map = folium.Map(location = [51.0447, -114.0719], zoom_start=12)
#Generating the map
map.save('CalgaryMap.html')