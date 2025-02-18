import pika
import json
import uuid
import redis
import logging
from config import RABBITMQ_URL, REDIS_HOST, REDIS_PORT

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue='order_queue', durable=True)

    def send_order(user_id, product, quantity):
        order_id = str(uuid.uuid4())
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "product": product,
            "quantity": quantity,
            "status": "Pending"
        }

        redis_client.hset(f"order:{order_id}", mapping=order)

        channel.basic_publish(
            exchange='',
            routing_key='order_queue',
            body=json.dumps(order),
            properties=pika.BasicProperties(delivery_mode=2) 
        )

        print(f"Order {order_id} sent to queue")
        return order_id
except Exception as e:
    logging.error(f"Failed to send order: {e}")

if __name__ == "__main__":
    send_order("user123", "Laptop", 1)
