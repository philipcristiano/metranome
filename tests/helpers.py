from metranome.amqp_connection import AMQPConnection

def amqp_connection_from_config(config):
    host = 'amqp://{0}'.format(config['rabbitmq']['host'])
    return AMQPConnection(host)
