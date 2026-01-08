import requests


def send_telegram_message(CHAT_ID, MESSAGE_TEXT):
    BOT_TOKEN = '8328745194:AAGXTBuUOsKhK-GMlmakZU8Pccfu_JgyYvI'

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': MESSAGE_TEXT}

    response = requests.post(url, data=data)
    print(response.json())
