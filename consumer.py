from  kafka import KafkaConsumer
import json
consumer = KafkaConsumer("Quotes",bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',auto_commit_interval_ms=1000,
                         group_id='my-group',enable_auto_commit=True)

for quote in consumer:
    print("New Quotes : ",json.loads(quote.value))