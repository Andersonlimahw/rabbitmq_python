#!/usr/bin/env python
import pika
import time
import requests
import json

def callback(ch, method, properties, body):
	try:
		print(" [x] Received message: %r" % body)
		json_result = json.loads(body)

		print("============================")
		url = json_result["homeworld"]
		print(" [x] Loading homeworld to %r" % json_result["name"])
		world = requests.get(url);
		print(" [x] Returned world: %r" % world.text)
		print("============================")
		
		ch.basic_ack(delivery_tag = method.delivery_tag)
		print(" [x] Success on message process to  %r: " %json_result["name"])
	except Exception as ex:
		print("Fail to execute message.")
		print(ex)
	finally:
		print(" [x] Callback finished!")
		print("============================")
	

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='star_wars_people_events')

channel.basic_consume(queue='star_wars_people_events',
                      auto_ack=False,
                      on_message_callback=callback)
					  
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
