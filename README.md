# Pi_MQTT_Softener_Sensor
<img width=400px src="https://1.bp.blogspot.com/-F2rXYfAIOEc/YX7KNLvLqzI/AAAAAAADJnM/aOAcIuVaH1o9GbwqdOzH94Dmtd5BpjLrwCLcBGAsYHQ/s2543/20211029_233734.jpg">

## Install Dependencies
More information here: http://www.steves-internet-guide.com/into-mqtt-python-client/
```
pip install paho-mqtt
```

## Update script with MQTT host, user, and password
Update the following values in salt_monitor.py to meet your needs.
```yaml
mqttBroker = "<% MQTT_HOST %>"
mqttTopic = "home/pi/softener"
mqttUser = "homeassistant"
mqttPassword = "<% MQTT_PASSWORD %>"
```

## Run script
```
python salt_monitor.py
```
