import time
from kafka import KafkaProducer
import json
import requests

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

print("\tProducing random quotes and storing in topic Quotes.\n")
while True:
    resp = requests.get('https://goquotes-api.herokuapp.com/api/v1/random?count=1')
    data = json.loads(resp.text)
    data_quotes = data.get('quotes')[0]
    quote = data_quotes.get('text')
    producer.send("Quotes",value=quote)
    print(quote,"\nquote addded to the topic\n")
    time.sleep(3)