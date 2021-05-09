from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='localhost:9092')
msg='as'
encoded_string = msg.encode()
byte_array = bytearray(encoded_string)
producer.send('Hello-Kafka', byte_array)
