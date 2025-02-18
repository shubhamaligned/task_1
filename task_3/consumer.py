import pika
import json
import redis
import logging
from config import RABBITMQ_URL, REDIS_HOST, REDIS_PORT
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()
channel.queue_declare(queue='order_queue', durable=True)

def process_order(ch, method, properties, body):
    try:
        order = json.loads(body)
        order_id = order["order_id"]

        logging.info(f"Processing order {order_id}")

        redis_client.hset(f"order:{order_id}", "status", "Processing")
        redis_client.hset(f"order:{order_id}", "status", "Completed")

        channel.basic_publish(
            exchange='',
            routing_key='notification_queue',
            body=json.dumps(order),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        ch.basic_ack(delivery_tag=method.delivery_tag)
        logging.info(f"Order {order_id} processed successfully")

    except Exception as e:
        logging.error(f"Error processing order: {e}")

channel.basic_consume(queue='order_queue', on_message_callback=process_order)
print("Waiting for orders...")
channel.start_consuming()
