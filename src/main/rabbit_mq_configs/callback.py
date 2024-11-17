import json
from src.drivers.telegram_sender import send_telegram_message


def rabbit_mq_callback(ch, method, properties, body):
    msg = body.decode("uft-8")
    formatted_msg = json.loads(msg)
    telegram_message = formatted_msg["msg"]

    send_telegram_message(telegram_message)
