import datetime
import time

from pika.adapters import BlockingConnection
from pika import BasicProperties, ConnectionParameters


class AMQPMetranome(object):
    pass

class AMQPConnection(object):

    def __init__(self):
        self.connection = BlockingConnection(
            ConnectionParameters(host='33.33.33.10')
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='metranome', type='topic')
        self.queue = self.channel.queue_declare(queue='metranome', exclusive=True, auto_delete=False)

    def run(self):
        while True:
            now = datetime.datetime.utcnow()
            self._tick()
            time.sleep(5)

    def _tick(self, datetime):

        self.channel.basic_publish(
            exchange='metranome',
            routing_key= self._datetime_to_routing_key(datetime),
            body='',
            properties=BasicProperties(
                content_type='text/plain',
                delivery_mode=1
            )
        )

    def _datetime_to_routing_key(self, dt):
        return '{0}.{1}.{2}.{3}.{4}'.format(
           dt.year,
           dt.month,
           dt.day,
           dt.hour,
           dt.minute
        )
