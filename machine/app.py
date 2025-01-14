import pika
import os
import logging
import socket
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# RabbitMQ connection parameters
rabbitmq_host = os.getenv('RABBITMQ_HOST', 'rabbitmq')
rabbitmq_queue = os.getenv('RABBITMQ_QUEUE', 'training')

# Get the hostname of the machine
hostname = socket.gethostname()

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    action = message.get("action")
    logger.info(f"Machine {hostname} received message: {message}")
    # Process the message here
    if action == "start_training":
        logger.info(f"Machine {hostname} is starting training for user {message['userid']} with trainingset {message['trainingsetid']}...")
    elif action == "stop_training":
        logger.info(f"Machine {hostname} is stopping training {message['trainingid']}...")
    elif action == "status_training":
        logger.info(f"Machine {hostname} is checking training status...")
    elif action == "generate":
        logger.info(f"Machine {hostname} is generating data...")
    else:
        logger.warning(f"Machine {hostname} received unknown action: {action}")

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.exchange_declare(exchange='training_exchange', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='training_exchange', queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    logger.info(f"Machine {hostname} is waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()