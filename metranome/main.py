from datetime import datetime
from time import sleep

from metranome.nome import Metranome
from metranome.timer import MinuteTimer
from metranome.amqp_connection import AMQPConnection


def run_all_the_frickin_time():
    return True


def main():
    timer = MinuteTimer(datetime.utcnow, sleep)
    connection = AMQPConnection()
    metranome = Metranome(connection, timer, continue_policy=run_all_the_frickin_time)
    metranome.run()


if __name__ == '__main__':
    main()
