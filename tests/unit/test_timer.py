from datetime import datetime

from mock import MagicMock
from unittest2 import TestCase

from metranome.timer import MinuteTimer


class TestMinuteTimer(TestCase):

    def setUp(self):
        self.get_current_time = MagicMock()
        self.sleep_func = MagicMock()

        self.timer = MinuteTimer(self.get_current_time, self.sleep_func)

    def should_sleep_until_next_minute_when_2_seconds_until(self):
        now = datetime(2012, 8, 5, 17, 0, 58)
        self.get_current_time.return_value = now
        self.timer.wait()

        self.sleep_func.assert_called_once_with(2)

    def should_sleep_until_next_minute_when_1_seconds_until(self):
        now = datetime(2012, 8, 5, 17, 0, 59)
        self.get_current_time.return_value = now
        self.timer.wait()

        self.sleep_func.assert_called_once_with(1)

    def should_sleep_for_a_minute_if_on_the_minute(self):
        now = datetime(2012, 8, 5, 17, 0, 0)
        self.get_current_time.return_value = now
        self.timer.wait()

        self.sleep_func.assert_called_once_with(60)

    def should_handle_hour_rollover(self):
        now = datetime(2012, 8, 5, 17, 59, 30)
        self.get_current_time.return_value = now
        self.timer.wait()

        self.sleep_func.assert_called_once_with(30)

    def should_handle_day_rollover(self):
        now = datetime(2012, 8, 5, 23, 59, 35)
        self.get_current_time.return_value = now
        self.timer.wait()

        self.sleep_func.assert_called_once_with(25)
