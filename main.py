import sys
from Adafruit_IO import MQTTClient
import time
import random
# from simple_ai import *
from uart import *
import datetime
AIO_FEED_ID = ["nutnhan1", "nutnhan2","nutnhan3"]
AIO_USERNAME = "todiuquang123"
AIO_KEY = "aio_Youu88rmfLJcUtMuFUwyoKxkWMmb"

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
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter=10
counter_time = 1
# # sensor_type=0
# counter_ai =5
# ai_result =""
# pre_result =""
while True:
    counter = counter -1
    if counter <=0:
        counter =10
        print("Random data is publishing...")
        temp = random.randint(10,20)
        client.publish("cambien1", temp)
        humi = random.randint(40,60)
        client.publish("cambien2", humi)
    counter_time = counter_time - 1
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if counter_time <= 0:
        counter_time = 1
        if current_time == "17:00:00":
            client.publish("nutnhan1",1)
    # counter_ai= counter_ai-1
    # if counter_ai<=0:
    #     counter_ai=5
    #     pre_result =ai_result
    #     ai_result = image_detector()
    #     print("AI output: ", ai_result)
    #     if pre_result != ai_result:
    #         client.publish("ai", ai_result)
    # readSerial(client)
    time.sleep(1)
