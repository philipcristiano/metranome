from datetime import datetime, timedelta


class MinuteTimer(object):

    def __init__(self, current_time_func, sleep_func):
        self.current_time_func = current_time_func
        self.sleep_func = sleep_func
        self.time_delta = timedelta(minutes=1)

    def wait(self):
        now = self.current_time_func()
        a_minute_from_now = now + self.time_delta
        until = datetime(
            a_minute_from_now.year,
            a_minute_from_now.month,
            a_minute_from_now.day,
            a_minute_from_now.hour,
            a_minute_from_now.minute,
        )
        sleep_for = until - now
        self.sleep_func(total_seconds_for_timedelta(sleep_for))
        return until

def total_seconds_for_timedelta(td):
    """Convert a timedelta to total seconds.

    This is taken from
    http://docs.python.org/library/datetime.html#datetime.timedelta.total_seconds
    as `total_seconds` was added in 2.7

    """
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
