import click

from confluent_kafka import Producer


p = Producer({
    'bootstrap.servers': '13.49.128.80:19093,13.49.128.80:29093,13.49.128.80:39093',
    'security.protocol': 'SSL',
    'ssl.ca.location': './auth/ca.crt',
    'ssl.keystore.location': './auth/kafka.keystore.pkcs12',
    'ssl.keystore.password': 'cc2023',
    'ssl.endpoint.identification.algorithm': 'none',
})

@click.command()
@click.argument('topic')
def produce(topic: str): 
    while True: 
        message = input()
        p.produce(topic, key="1", message.encode('utf-8'))
        p.flush()


produce()
