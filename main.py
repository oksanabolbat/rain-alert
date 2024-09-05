# import geopy
from geopy.geocoders import Nominatim
import requests

loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Milano")
lat = getLoc.latitude
lon = getLoc.longitude

API_KEY = "1c2b12b217b5fc990842bf1f65eb7345"

URL_NEW = "https://api.openweathermap.org/data/3.0/onecall"

URL = "https://api.openweathermap.org/data/2.5/forecast"
api_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}
response = requests.get(URL, params=api_params)
response.raise_for_status()
data = response.json()
print(data)
weather_data = data["list"]
for hour_data in weather_data:
    if int(hour_data["weather"][0]["id"]) < 700:
        print("Bring an umbrella")
        break

