import requests
import urllib.parse

def send_telegram_msg(bot_message):
    bot_token = '6337817808:AAHR8bIWA9gu8J-9jybLD5TyiFgIwmSnzDE'
    bot_chatID = '654982046'
    encoded_msg = urllib.parse.quote(bot_message, safe='/', encoding=None, errors=None)
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + encoded_msg
    response = requests.get(send_text)

    return response.json()