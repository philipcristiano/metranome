import datetime
from unittest2 import TestCase
import time

from pika.adapters import BlockingConnection
from pika import BasicProperties, ConnectionParameters

from metranome.amqp_connection import AMQPConnection


class Consumer(object):
    def __init__(self):
        self.connection = BlockingConnection(
            ConnectionParameters(host='33.33.33.10')
        )
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue='test_metranome', exclusive=True, auto_delete=False)
        self.channel.queue_bind(exchange='metranome', queue='test_metranome', routing_key='#')

    def get(self):
        print self.channel.basic_get(queue='test_metranome', no_ack=True)


class TestAMQPConnection(TestCase):

    def setUp(self):
        self.amqp_connection = AMQPConnection()
        self.consumer = Consumer()

    def test_amqp_tick(self):
        now = datetime.datetime(2012, 8, 5, 12, 1)
        self.amqp_connection._tick(now)
        time.sleep(.5)
        self.consumer.get()
