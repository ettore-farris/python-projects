from smtplib import *
from datetime import *
from random import *
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("my_email")
app_password = os.getenv("app_password")
to_address = os.getenv("to_address")
print(my_email)
print(app_password)

weekday = datetime.now().weekday()


def random_quote():
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        return choice(quotes)


if weekday == 4:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address,
                            msg=f"Subject: This is your Monday Quote\n\n{random_quote()}")
