#importing all the files required
import folium
import os
from geopy.geocoders import Nominatim

#initialising the Nomiantim to get the coordinates of the city
geolocator = Nominatim(user_agent="Map")

#finding the latitude and longitude of the location
x=input("Enter location:")
location = geolocator.geocode(x)
lat=location.latitude
long=location.longitude

#generating the map
_map=folium.Map(location=[lat,long])

#writing and opening the map
_map.save("map.html")
os.system("map.html")
print("Map has been made.")



