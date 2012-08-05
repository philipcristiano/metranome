from mock import MagicMock
from unittest2 import TestCase

from metranome.amqp_connection import AMQPConnection

class TestAMQPMetronome(TestCase):

    def setUp(self):
        self.amqp_connection = MagicMock(
            AMQPConnection,
            name='amqp_connection'
        )
        self.metranome = AMQPMetranome(self.amqp_connection)


