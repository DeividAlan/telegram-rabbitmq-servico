import os
import pika
from src.main.rabbit_mq_configs.callback import rabbit_mq_callback


class RabbitMQConsumer:
    def __init__(self) -> None:
        self.__host = os.getenv("RABBIT_MQ_HOST")
        self.__port = os.getenv("RABBIT_MQ_PORT")
        self.__username = os.getenv("RABBIT_MQ_USERNAME")
        self.__password = os.getenv("RABBIT_MQ_PASSWORD")
        self.__queue = os.getenv("RABBIT_MQ_BOT_QUEUE")
        self.__channel = self.create_channel()

    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username, password=self.__password
            ),
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(queue=self.__queue, durable=True)
        channel.basic_consume(
            queue=self.__queue, on_message_callback=rabbit_mq_callback, auto_ack=True
        )
        return channel

    def start(self):
        self.__channel.start_consuming()
