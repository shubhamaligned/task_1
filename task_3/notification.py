import pika
import json
import smtplib
from email.message import EmailMessage
from config import RABBITMQ_URL, EMAIL_SENDER, EMAIL_PASSWORD

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_URL))
channel = connection.channel()
channel.queue_declare(queue='notification_queue', durable=True)

def send_email_notification(user_email, order_details):
    msg = EmailMessage()
    msg['Subject'] = f"Order Confirmation - {order_details['order_id']}"
    msg['From'] = EMAIL_SENDER
    msg['To'] = user_email
    msg.set_content(f"Hello,\n\nYour order for {order_details['quantity']}x {order_details['product']} has been processed successfully!\n\nOrder ID: {order_details['order_id']}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Notification sent to {user_email} for order {order_details['order_id']}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def process_notification(ch, method, properties, body):
    order = json.loads(body)
    user_email = f"{order['user_id']}@example.com"

    send_email_notification(user_email, order)

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='notification_queue', on_message_callback=process_notification)
print("Waiting for notifications...")
channel.start_consuming()
