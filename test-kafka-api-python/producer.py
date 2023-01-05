from kafka import KafkaProducer

TOPIC_NAME = 'test-topic-python'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

for i in range(10):
    producer.send(TOPIC_NAME, b'Data send in python - %d' % (i+1))

producer.flush()
