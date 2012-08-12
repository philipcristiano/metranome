from datetime import datetime
from time import sleep

from mock import MagicMock, patch
from unittest2 import TestCase

from metranome.main import main, run_all_the_frickin_time


class TestMain(TestCase):

    @patch('metranome.main.Metranome')
    @patch('metranome.main.MinuteTimer')
    @patch('metranome.main.create_amqp_connection_from_config')
    @patch('metranome.main.config')
    def setUp(self, config, conn_factory, timer, nome):
        self.config = config
        self.mock_conn_factory = conn_factory
        self.timer = timer(datetime.utcnow, sleep)
        self.nome = nome
        main()

    def should_setup_metranome(self):
        self.nome.assert_called_once_with(self.mock_conn_factory(), self.timer, continue_policy=run_all_the_frickin_time)

    def should_run_metranomes_run_method(self):
        self.nome().run.assert_called_once_with()

    def should_create_amqp_connection_with_config(self):
        self.mock_conn_factory.assert_called_once_with(self.config)
