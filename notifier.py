import requests
from config import BOT_TOKEN, CHAT_ID

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=data)
    except Exception as e:
        print(f"Ошибка отправки уведомления: {e}")
