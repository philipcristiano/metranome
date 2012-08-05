from mock import MagicMock
from unittest2 import TestCase

from metranome.amqp_connection import AMQPConnection
from metranome.nome import Metranome
from metranome.exceptions import NotLockableException
from metranome.timer import MinuteTimer


class TestMetranome(TestCase):

    def setUp(self):
        self.continue_policy = MagicMock(side_effect=[True, False])
        self.mock_connection = MagicMock(AMQPConnection)
        self.timer = MagicMock(MinuteTimer)
        self.mn = Metranome(
            self.mock_connection,
            self.timer,
            self.continue_policy
        )

    def should_publish_datetime(self):
        self.mn.run()
        self.mock_connection.publish_datetime.assert_called_once_with(self.timer.wait())

class TestMetranomeWithoutLock(TestCase):

    def setUp(self):
        self.continue_policy = MagicMock(side_effect=[True, False])
        self.mock_connection = MagicMock(AMQPConnection)
        self.mock_connection.get_lock.side_effect=NotLockableException()
        self.timer = MagicMock()
        self.mn = Metranome(
            self.mock_connection,
            self.timer,
            self.continue_policy
        )

    def test_should_stop_running(self):
        self.assertEqual(self.mn.run(), False)



