from src.main.rabbit_mq_configs.consumer import RabbitMQConsumer

if __name__ == "__main__":
    consumer = RabbitMQConsumer()
    consumer.start()
