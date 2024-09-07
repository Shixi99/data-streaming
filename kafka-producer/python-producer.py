import time
import random
import datetime
import schedule # type: ignore
from kafka import KafkaProducer  # type: ignore
from faker import Faker
from json import dumps


kafka_nodes = "kafka:9092"
myTopic="weather"

def gen_data():
    faker = Faker()
    prod = KafkaProducer(bootstrap_servers=kafka_nodes,
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
    my_data = {
        'city': faker.city(), 
        'temperature': random.uniform(1.0, 45.0)
    }
    print(my_data)
    prod.send(topic=myTopic, value=my_data)
    prod.flush()

if __name__=="__main__":
    gen_data()
    schedule.every(5).seconds.do(gen_data)

    while True:
        schedule.run_pending()
        time.sleep(5)


