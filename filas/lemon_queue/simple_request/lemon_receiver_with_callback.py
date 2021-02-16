#!/usr/bin/env python
import pika
import time
import requests

def callback(ch, method, properties, body):
	try:
		print(" [x] Received message: %r" % body)
		person = requests.get(body);

		time.sleep(1);
		print(person.text);
		print(" [x] Success")
		ch.basic_ack(delivery_tag = method.delivery_tag)
	except:
		print("As exception ocurred")
	finally:
		print("Callback finished!")
	

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='star_wars_events')

channel.basic_consume(queue='star_wars_events',
                      auto_ack=False,
                      on_message_callback=callback)
					  
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
