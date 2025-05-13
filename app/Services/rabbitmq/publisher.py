import pika
import json

RABBITMQ_URL = 'amqp://guest:guest@localhost:5672/'
QUEUE_NAME = 'player.created'

def publish_player_created(player_data):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    message = json.dumps(player_data)
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          body=message.encode(),
                          properties=pika.BasicProperties(
                              delivery_mode=2, 
                          ))

    print(f"[x] Sent message to queue {QUEUE_NAME}: {message}")

    connection.close()
