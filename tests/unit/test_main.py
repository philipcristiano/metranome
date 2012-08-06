from datetime import datetime
from time import sleep

from mock import MagicMock, patch
from unittest2 import TestCase

from metranome.main import main, run_all_the_frickin_time


class TestMain(TestCase):

    @patch('metranome.main.Metranome')
    @patch('metranome.main.MinuteTimer')
    @patch('metranome.main.AMQPConnection')
    def setUp(self, connection, timer, nome):
        self.connection = connection()
        self.timer = timer(datetime.utcnow, sleep)
        self.nome = nome
        main()

    def should_setup_metranome(self):
        self.nome.assert_called_once_with(self.connection, self.timer, continue_policy=run_all_the_frickin_time)

    def should_run_metranomes_run_method(self):
        self.nome().run.assert_called_once_with()
