#!/usr/bin/env python
import pika
import time
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='star_wars_events')
peoples = [
	"1", 
	"2", 
	"3", 
	"4", 
	"5", 
	"6", 
	"7", 
	"8", 
	"9", 
	"10", 
	"11", 
	"12"
];

messages = [];
try:
	print("[X] Loading person")
	for person in peoples:
		url = "https://swapi.dev/api/people/" + person;
		result = requests.get(url);
		messages.append(result.text)

	print("[X] Adding person %r to messages: " % person)
	for message in messages:
		channel.basic_publish(exchange='',
							routing_key='star_wars_people_events',
							body=message)
		print(" [x] Message sent to  queue [star_wars_people_events] '" + message + "'")
		time.sleep(1)
except Exception as ex:
	print(" [x] Fail to process message.")
	print(ex)
finally:
	print(" [x] Process finished to queued [star_wars_people_events]!")
	connection.close()
