from twilio import Client

account_sid = "YOUR ACCOUNT SID HERE"
auth_token = "YOUR API KEY HERE"

client = Client(account_sid, auth_token)

def send_sms():
    message = client.messages \
        .create(
            body= "Weather's gonna be like ew Today. Bring an umbrella!",
            from_= "TWILIO NUMBER HERE",
            to="YOUR NUMBER HERE"
        )
