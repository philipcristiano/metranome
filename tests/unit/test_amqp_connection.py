from mock import patch, MagicMock
from unittest2 import TestCase

from metranome.amqp_connection import AMQPConnection

class TestAMQPConnection(TestCase):

    @patch('metranome.amqp_connection.puka')
    def setUp(self, mock_puka):
        self.mock_puka = mock_puka
        self.host = 'HOST'

        self.amqpc = AMQPConnection(self.host)

    def should_create_client_with_host(self):
        self.mock_puka.Client.assert_called_once_with(self.host)
