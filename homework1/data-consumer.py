from kafka import KafkaConsumer
consumer  = KafkaConsumer('average-stock-price',
                  bootstrap_servers  = "192.168.99.100:9092",
                  auto_offset_reset ='earliest')
for message in consumer:
    print(message)

