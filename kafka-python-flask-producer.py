from flask import Flask
from kafka import KafkaProducer
app = Flask(__name__)

@app.route('/publish/<msg>')
def hello_world(msg):
   producer = KafkaProducer(bootstrap_servers='localhost:9092')
   encoded_string = msg.encode()
   byte_array = bytearray(encoded_string)
   producer.send('Hello-Kafka', byte_array)
   return "published message " + msg + " successfully"


if __name__ == '__main__':
   app.run()
