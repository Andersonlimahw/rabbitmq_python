#!/usr/bin/env python
import pika

def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='star_wars_events')

channel.basic_consume(queue='star_wars_events',
                      auto_ack=True,
                      on_message_callback=callback)
					  
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
