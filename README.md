dc up -d

# Create topics
```bash
dc exec kafka bash
kafka-topics.sh --create --topic topic1 --bootstrap-server kafka1:9091
kafka-topics.sh --create --topic topic2 --bootstrap-server kafka2:9092
```

# Produce messages
```bash
dc exec kafka bash
kafka-console-producer.sh --topic <topic1 or topic2> --bootstrap-server kafka1:9091
kafka-console-producer.sh --topic <topic1 or topic2> --bootstrap-server kafka2:9092
```

# Consume messages
```bash
dc exec kafka bash
kafka-console-consumer.sh --topic <topic1 or topic2> --bootstrap-server kafka1:9091
kafka-console-consumer.sh --topic <topic1 or topic2> --bootstrap-server kafka2:9092
```

# Use python to produce and consume messages to save them in mongodb
```bash
dc up -d
dc run --rm python bash
cd /app/src
python3 producer.py&
python3 consumer.py
# and open localhost:8081 to see the messages in mongodb.
```
