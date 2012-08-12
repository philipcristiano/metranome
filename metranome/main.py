from datetime import datetime
from time import sleep

from metranome.amqp_factory import create_amqp_connection_from_config
from metranome.config import config
from metranome.nome import Metranome
from metranome.timer import MinuteTimer


def run_all_the_frickin_time():
    return True


def main():
    timer = MinuteTimer(datetime.utcnow, sleep)
    connection = create_amqp_connection_from_config(config)
    metranome = Metranome(connection, timer, continue_policy=run_all_the_frickin_time)
    metranome.run()


if __name__ == '__main__':
    main()
