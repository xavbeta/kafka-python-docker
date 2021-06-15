from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
for j in range(9):
    print("Iteration", j)
    data = {'counter': j}
    future = producer.send('test_events', value=data)
    result = future.get(timeout=30)
    #sleep(0.5)