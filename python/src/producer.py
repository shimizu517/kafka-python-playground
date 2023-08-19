from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers=['kafka1:9091'],
    client_id='test'
)

try:
  admin_client.create_topics(
      new_topics=[
        NewTopic(name='topic1', num_partitions=1, replication_factor=1)
      ],
      validate_only=False,
  )
except Exception as e:
  print(e)

producer = KafkaProducer(
    bootstrap_servers=['kafka1:9091'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

for i in range(10 ** 7):
    data = {'number': i}
    producer.send('topic1', value=data)
    sleep(5)
