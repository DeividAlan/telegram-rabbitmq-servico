# Telegram Bot with RabbitMQ Integration

## **Overview**

This project is a Telegram bot integrated with RabbitMQ for efficient message processing and communication. It uses the Telegram API to send messages and RabbitMQ to manage message queues. The bot listens for messages from RabbitMQ, processes them, and sends them to a specified Telegram chat.

---

## **Features**

- **RabbitMQ Consumer**: Listens to a specific RabbitMQ queue for incoming messages.
- **RabbitMQ Publisher**: Publishes messages to an exchange.
- **Telegram Integration**: Sends messages to a Telegram chat via the Telegram Bot API.
- **Environment Variable Configuration**: Flexible setup for hostnames, tokens, and credentials.

---

## **Requirements**

- Python 3.9+
- RabbitMQ
- A Telegram bot token (generated via [BotFather](https://t.me/BotFather))

---

## **Installation**

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

  Create a `.env` file in the root directory with the following variables:
   ```env
   TELEGRAM_TOKEN=<your-telegram-bot-token>
   TELEGRAM_CHAT_ID=<your-chat-id>
   RABBIT_MQ_HOST=<rabbitmq-host>
   RABBIT_MQ_PORT=<rabbitmq-port>
   RABBIT_MQ_USERNAME=<rabbitmq-username>
   RABBIT_MQ_PASSWORD=<rabbitmq-password>
   RABBIT_MQ_BOT_QUEUE=<queue-name>
   RABBIT_MQ_BOT_EXCHANGE=<exchange-name>
   ```

---
   
## **Usage**

### **Starting the RabbitMQ Consumer**
To start the bot and process incoming messages from RabbitMQ, run:

   ```bash
   python run.py
   ```

- The consumer listens for messages on the configured RabbitMQ queue (on ports `5672` for AMQP and `15672` for the management console).
- When a message is received, it is sent to the specified Telegram chat.

---

## **Sending Messages to RabbitMQ**
To send a message through RabbitMQ (and eventually to Telegram), use the RabbitMQ Publisher:

   ```python
   from src.rabbitmq_publisher import RabbitMQPublisher

   publisher = RabbitMQPublisher()
   publisher.send_message({"msg": "Hello from RabbitMQ!"})
   ```

---

## **Environment Configuration**

All sensitive or environment-specific configurations are stored in environment variables for security and flexibility. You can set these variables using a `.env` file or directly in your system.