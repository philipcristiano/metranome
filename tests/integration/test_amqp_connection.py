import datetime
from unittest2 import TestCase
import time

from pika.adapters import BlockingConnection
from pika import BasicProperties, ConnectionParameters

from metranome.amqp_connection import AMQPConnection
from metranome.config import config
from metranome.nome import NotLockableException
from metranome.amqp_factory import create_amqp_connection_from_config


class Consumer(object):
    def __init__(self, routing_key):
        self.connection = BlockingConnection(
            ConnectionParameters(host='33.33.33.10')
        )
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue='test_metranome', exclusive=True, auto_delete=False)
        self.channel.queue_bind(exchange='metranome', queue='test_metranome', routing_key=routing_key)

    def get(self):
        return self.channel.basic_get(queue='test_metranome', no_ack=True)


class TestAMQPConnection(TestCase):

    def setUp(self):
        self.dt_list = [2012, 8, 5, 12, 1]
        self.routing_key = '2012.8.5.6.12.1'
        self.amqp_connection = create_amqp_connection_from_config(config)
        self.consumer = Consumer(self.routing_key)

    def test_amqp_tick(self):
        now = datetime.datetime(*self.dt_list)
        self.amqp_connection._tick(now)
        time.sleep(.5)
        method, header, body = self.consumer.get()
        rk = str(method.routing_key)
        str_dt = map(str, self.dt_list)
        self.assertEqual(rk, self.routing_key)


class TestAMQPConnectionLocking(TestCase):

    def setUp(self):
        self.amqp_connection = create_amqp_connection_from_config(config)
        self.amqp_connection2 = create_amqp_connection_from_config(config)

    def test_amqp_lock(self):
        self.amqp_connection.get_lock()
        self.assertRaises(NotLockableException, self.amqp_connection2.get_lock)



