# Pi_MQTT_Softener_Sensor
<img width=400px src="https://1.bp.blogspot.com/-F2rXYfAIOEc/YX7KNLvLqzI/AAAAAAADJnM/aOAcIuVaH1o9GbwqdOzH94Dmtd5BpjLrwCLcBGAsYHQ/s2543/20211029_233734.jpg">

## Install Dependencies
More information here: http://www.steves-internet-guide.com/into-mqtt-python-client/
```
pip install paho-mqtt
```

## Update script with MQTT host, user, and password
Update the following MQTT configuration values:
```yaml
#MQTT constants
mqttBroker = "<% MQTT_HOST %>"
mqttTopic = "home/pi/softener"
mqttUser = "homeassistant"
mqttPassword = "<% MQTT_PASSWORD %>"
```
Update the sensor pins to match how you wired your sensor
```yaml
#sensor constants
TRIG = 23
ECHO = 24
```

Update the following distances to match your specific brine tank measurements
```yaml
#measurements constants
TANK_EMPTY_DISTANCE = 31 #inches
TANK_FULL_DISTANCE = 6 #inches
TANK_LOW_WATERMARK_DISTANCE = 25 #inches
```

## Run script
```
python salt_monitor.py
```
