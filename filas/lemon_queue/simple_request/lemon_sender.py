#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='star_wars_events')

messages = ["https://swapi.dev/api/people/1/", "https://swapi.dev/api/planets/1", "https://swapi.dev/api/vehicles/1"];
for message in messages:
	channel.basic_publish(exchange='',
						  routing_key='star_wars_events',
						  body=message)
	print(" [x] Enviada '" + message + "'")
	time.sleep(1)

connection.close()