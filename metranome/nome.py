

class NotLockableException(Exception):
    pass

class Metranome(object):

    def __init__(self, connection, timer, continue_policy):
        self._connection = connection
        self._timer = timer
        self._continue_policy = continue_policy

    def run(self):
        try:
            self._connection.get_lock()
        except NotLockableException:
            return False

        while self._continue_policy():
            self._connection.publish_datetime(self._timer())

