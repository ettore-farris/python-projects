from smtplib import *
from datetime import *
from pandas import *
from random import *

MY_EMAIL = "YOUR EMAIL HERE"
APP_PASSWORD = "YOUR PASSWORD HERE"
TODAY = (datetime.now().day, datetime.now().month)
birthdays = read_csv("birthdays.csv").to_dict(orient="records")

#function to send email using smtplib
             
def send_email(name, email, letter_content):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=email, 
                            msg=f"Subject: Happy Birthday {name}!\n\n{letter_content}")      

#loop to look for the birtday boys 
       
for i in birthdays:
    name = i["name"]
    email = i["email"]
    day = i["day"]
    month = i["month"]
    
    if day and month in TODAY:
        random_letter = f"letter_templates\letter_{randint(1,3)}.txt"     
        with open(random_letter) as letter_file:
            letter_content = letter_file.read()
            letter_content = letter_content.replace("[NAME]", name)    
            print(email, name)
        send_email(name, email, letter_content)
