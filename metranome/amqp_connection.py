import datetime
import time

import puka


class AMQPMetranome(object):
    pass

class AMQPConnection(object):

    def __init__(self):
        self._client = puka.Client("amqp://33.33.33.10/")
        promise = self._client.connect()
        time.sleep(.1)
        self._client.wait(promise)

        promise = self._client.exchange_declare(
            'metranome',
            type='topic'
        )
        self._client.wait(promise)

        promise = self._client.queue_declare(
            queue='metranome',
            exclusive=True
        )
        self._client.wait(promise)

    def run(self):
        while True:
            now = datetime.datetime.utcnow()
            self._tick()
            time.sleep(5)

    def _tick(self, datetime):
        promise = self._client.basic_publish(
            exchange='metranome',
            routing_key=self._datetime_to_routing_key(datetime),
            body='')
        self._client.wait(promise)

    def _datetime_to_routing_key(self, dt):
        return '{0}.{1}.{2}.{3}.{4}'.format(
           dt.year,
           dt.month,
           dt.day,
           dt.hour,
           dt.minute
        )
