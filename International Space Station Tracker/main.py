import requests
from datetime import datetime
from smtplib import *
import time

MY_LAT = 12.123456 #EXAMPLE
MY_LONG = 8.123456 #EXAMPLE
MY_EMAIL = "YOUR EMAIL HERE"
MY_PASSWORD = "YOUR PASSWORD HERE"


#check if the ISS is close to my position (+5 -5 degrees)
def is_iss_overhead():
    #api request to get ISS data
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if (MY_LAT - 5 >= iss_latitude <= MY_LAT - 5) and (MY_LONG -5 >= iss_longitude <= MY_LONG -5):
        return True


def is_now_dark():
    #api request to get the sunset/sunrise time based on my position
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    sun_response.raise_for_status()
    data = sun_response.json()
    current_hour = datetime.now().hour
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if (current_hour <= sunrise_hour) or (current_hour >= sunset_hour):
        return True
    
#email sender
while True:
    time.sleep(60)
    if is_now_dark() and is_iss_overhead():
        with SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(password=MY_PASSWORD, user=MY_EMAIL)
            connection.sendmail(to_addrs=MY_EMAIL,
                                from_addr=MY_EMAIL,
                                msg="Subject: La ISS sta passando da te\n\nHey guarda in alto! La stazione spaziale sta passando vicino a te!")




