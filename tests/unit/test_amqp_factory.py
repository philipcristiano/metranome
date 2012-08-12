from mock import patch, MagicMock
from unittest2 import TestCase

from metranome.amqp_factory import create_amqp_connection_from_config

class TestCreateAMQPConnectionFromCongi(TestCase):

    @patch('metranome.amqp_factory.AMQPConnection')
    def setUp(self, mock_amqp_connection):
        self.mock_amqp_connection = mock_amqp_connection
        self.mock_config = MagicMock()

        self.returned = create_amqp_connection_from_config(self.mock_config)

    def should_return_a_connection(self):
        self.assertEqual(self.returned, self.mock_amqp_connection())

    def should_create_connection_with_config_host(self):
        amqp_string = 'amqp://{0}/'.format(self.mock_config['rabbitmq']['host'])
        self.mock_amqp_connection.assert_called_once_with(amqp_string)

