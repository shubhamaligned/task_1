# Order Processing System (RabbitMQ + Redis)

## Overview
This project implements a simple **Order Processing System** using **RabbitMQ** as a message broker and **Redis** as a message store.

The system supports:
- Placing orders via a producer
- Processing orders via a consumer
- Sending email notifications via a notification consumer

## Architecture
- **Producer**: Sends orders to `order_queue` (RabbitMQ)
- **Order Consumer**: Processes orders and updates order status in Redis
- **Notification Consumer**: Sends email notifications when an order is completed

## Dependencies
- Python 3.8+
- RabbitMQ
- Redis
- Pika (for RabbitMQ communication)
- Redis-Py (for Redis communication)
- Email-Validator (for validating email addresses)

## Installation

### **1. Install Dependencies**
```sh
pip install pika redis email-validator

docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

docker run -d --name redis -p 6379:6379 redis

```

### **2. Start RabbitMQ and Redis**
#### Linux (Ubuntu/Debian)
```sh
sudo systemctl start rabbitmq-server
sudo systemctl start redis-server
```

#### Windows
- Start RabbitMQ and Redis manually from their installation directories.

### **3. Run the Application**
Open **three** separate terminal windows and run the scripts in this order:

#### **Start the Order Producer**
```sh
python producer.py
```
(Sends an order to RabbitMQ)

#### **Start the Order Consumer**
```sh
python consumer.py
```
(Processes orders from RabbitMQ and updates Redis)

#### **Start the Notification Consumer**
```sh
python notification.py
```
(Sends email notifications to users)

## **How It Works**
1. **Producer (`producer.py`)** sends an order to RabbitMQ.
2. **Consumer (`consumer.py`)** processes the order, updates its status in Redis, and sends a notification message to `notification_queue`.
3. **Notification Consumer (`notification.py`)** listens to `notification_queue` and sends an email notification to the user.

## **Environment Variables**
To use email notifications, configure your email credentials in `config.py`:
```python
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_PASSWORD = "your-email-password"
```
For Gmail, use an **App Password** instead of your regular password.

## **Future Enhancements**
- Implement a web UI to place and track orders

## **License**
MIT License

