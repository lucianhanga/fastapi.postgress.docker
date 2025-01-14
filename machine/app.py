import pika
import os
import logging
import socket

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# RabbitMQ connection parameters
rabbitmq_host = os.getenv('RABBITMQ_HOST', 'rabbitmq')
rabbitmq_queue = os.getenv('RABBITMQ_QUEUE', 'training')

# Get the hostname of the machine
hostname = socket.gethostname()

def callback(ch, method, properties, body):
    message = body.decode()
    logger.info(f"Machine {hostname} received message: {message}")
    # Process the message here
    if message == "start training":
        logger.info(f"Machine {hostname} is starting training...")
    elif message == "stop training":
        logger.info(f"Machine {hostname} is stopping training...")
    elif message == "status training":
        logger.info(f"Machine {hostname} is checking training status...")
    elif message == "generate":
        logger.info(f"Machine {hostname} is generating data...")

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=rabbitmq_queue)
    channel.basic_consume(queue=rabbitmq_queue, on_message_callback=callback, auto_ack=True)
    logger.info(f"Machine {hostname} is waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()
    
