import requests
from sms_sender import send_sms

endpoint = f"https://api.openweathermap.org/data/2.8/onecall"
params = {
    "appid": "YOUR APP ID HERE",
    "lat": 40.548360,
    "lon": 8.833080,
    "exclude": "minutely,current,daily"
}

response = requests.get(url=endpoint, params=params)
response.raise_for_status()
hourly_weather = response.json()["hourly"]

will_rain = False
for i in range(0,11):
    id = hourly_weather[i]["weather"][0]["id"]
    if id < 700:
        will_rain = True

if will_rain:
    send_sms()
    
