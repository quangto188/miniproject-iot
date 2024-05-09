import sys
import datetime
from Adafruit_IO import MQTTClient
import time
# from simple_ai import *
from uart import *
AIO_FEED_ID = ["nutnhan1", "nutnhan2","nutnhan3"]
AIO_USERNAME = "todiuquang123"
AIO_KEY = "aio_oRDa290TjTmnnoYvRkuhqgvqtXcN"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " ,feed id:"  + feed_id)
   
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter_time = 1
while True:
    counter_time = counter_time - 1
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if counter_time <= 0:
        counter_time = 1
        if current_time == "17:00:00":
            client.publish("nutnhan1",1)
    readSerial(client)
    time.sleep(1)
