import paho.mqtt.client as mqtt 
import RPi.GPIO as GPIO
import time
from datetime import datetime
from random import randrange, uniform
import time

#MQTT constants
mqttBroker = "<% MQTT_HOST %>"
mqttTopic = "home/pi/softener"
mqttUser = "homeassistant"
mqttPassword = "<% MQTT_PASSWORD %>"
client = mqtt.Client("Pi_MQTT_Softener_Sensor") # name is used by the MQTT broker to identify the client

#sensor constants
TRIG = 23
ECHO = 24
TANK_EMPTY_DISTANCE = 31 #inches
TANK_FULL_DISTANCE = 6 #inches
TANK_LOW_WATERMARK_DISTANCE = 25 #inches

sleep_duration = 60 #seconds

GPIO.setmode(GPIO.BCM)

def initialize():
   print "intitializing..."
   GPIO.setup(TRIG,GPIO.OUT)
   GPIO.setup(ECHO,GPIO.IN)

   GPIO.output(TRIG, False)
   print "Waiting for sensor to settle"
   time.sleep(2)
   connect_mqtt()

def connect_mqtt():
    print "connecting"
    client.username_pw_set(username=mqttUser,password=mqttPassword)
    client.on_connect=on_connect
    client.on_log=on_log
    client.connect(mqttBroker, 1883)

def get_distance_from_sensor():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    return distance

def monitor_loop():
    while 1==1:
        metric_distance = get_distance_from_sensor()
        imperial_distance = metric_distance / 2.54
        now = datetime.now()
	capacity = 0 if imperial_distance > TANK_EMPTY_DISTANCE else round(100 - (imperial_distance - TANK_FULL_DISTANCE) / (TANK_EMPTY_DISTANCE - TANK_FULL_DISTANCE) * 100, 1)

        log =  "%s Distance: %s inches - capacity: %s%%" % (now, imperial_distance, capacity)

	status = "";
        if capacity <= 15: #imperial_distance > TANK_EMPTY_DISTANCE:
	    print log, "*** Salt level is EMPTY ***"
            status = "empty"
	elif capacity > 15 and capacity < 36: #imperial_distance > TANK_LOW_WATERMARK_DISTANCE:
            print log, "*** Salt level is low ***"
	    status = "low"
        else:
            print log, "Salt level in acceptable range"
	    status = "good"

        message = "{\"softener_sensor_1\":{\"distance\": " + str(imperial_distance) + ", \"capacity\": " + str(capacity) + ", \"status\": \"" + str(status) + "\"}}"
	print message

        client.publish(mqttTopic, message)

        time.sleep(sleep_duration)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    monitor_loop()

def on_log(client, userdata, level, buf):
    print("log: ",buf)
    
try:
    initialize()
    monitor_loop()
finally:
   GPIO.cleanup();
