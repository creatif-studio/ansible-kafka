#!/usr/bin/env python3

from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
            bootstrap_servers="localhost:9092", 
                )

topic_list = []
topic_list.append(NewTopic(name="test-topic-python", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
