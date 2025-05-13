import pika
import json

RABBITMQ_URL = 'amqp://guest:guest@localhost:5672/'
QUEUE_NAME = 'player.created'

def callback(ch, method, properties, body):
    player_data = json.loads(body)
    print(f"[x] Received player created: {player_data}")

    # Exemplo de validação
    if "id" in player_data and "name" in player_data and "email" in player_data:
        print("Player data is valid.")
    else:
        print("Invalid player data structure.")

    # Confirma que processou a mensagem
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    print(f"[*] Waiting for messages in {QUEUE_NAME}. To exit press CTRL+C")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
