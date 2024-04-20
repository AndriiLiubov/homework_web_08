from faker import Faker

import pika

import conf.connect as connect
from conf.models import Contact

fake = Faker()


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

exchange = "send_email_exchange"
queue_name = "send_email_queue"

channel.exchange_declare(exchange=exchange, exchange_type="direct")
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange, queue=queue_name)

def create_tasks(nums):
    for i in range(nums):
        task = Contact(fullname=fake.name(), email=fake.email()).save()

        channel.basic_publish(
            exchange=exchange,
            routing_key=queue_name,
            body=str(task.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    connection.close()



if __name__ == "__main__":
    create_tasks(10)