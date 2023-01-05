from kafka import KafkaConsumer

TOPIC_NAME = 'test-topic-python'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print(str(message.value,'utf-8'))
