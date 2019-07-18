# hue
Python scripts to read and plot hue sensors.
Follow the official instructions at https://developers.meethue.com/develop/get-started-2/ to create a username for your Philips Hue bridge. This is needed to access the API.

## Install packages
```python
pip install -r requirements.txt
```

## Config
open Hue.py and insert the username for your bridge the names of your sensor

## Run
```bash
./Hue.py
```

## Plot
The following command plots the values of motion, light and temperature:
```bash
./plot.py
```
<img src="https://github.com/TobiasWeis/hue/raw/master/images/kitchen_motion.png" width="230">
<img src="https://github.com/TobiasWeis/hue/raw/master/images/kitchen_light.png" width="230">
<img src="https://github.com/TobiasWeis/hue/raw/master/images/kitchen_temp.png" width="230">


## TODO
- [ ] Put sensor-names in config
- [ ] Autodiscovery for sensors
- [ ] Web-back/front-end for plotting

### Sensor autodiscovery
Sensors can be merged based on their uniqueid, only the last three digits are different for motion,temp and light sensor:
```json
    "uniqueid": "00:17:88:01:04:b7:75:2e-02-0406"
		 00:17:88:01:04:b7:75:2e-02-0402 - temperature sensor 2
		 00:17:88:01:04:b7:75:2e-02-0400 - ambient light sensor 2
```


## Hue messages

This section contains some of the dumped JSON responses for later

### Motion sensor (+temperature sensor +ambient light sensor)
```json
{
    "capabilities": {
        "certified": true, 
        "primary": true
    }, 
    "config": {
        "alert": "none", 
        "battery": 100, 
        "ledindication": false, 
        "on": true, 
        "pending": [], 
        "reachable": true, 
        "sensitivity": 2, 
        "sensitivitymax": 2, 
        "usertest": false
    }, 
    "manufacturername": "Philips", 
    "modelid": "SML001", 
    "name": "Garderobe Sensor", 
    "productname": "Hue motion sensor", 
    "state": {
        "lastupdated": "2019-07-18T05:11:26", 
        "presence": false
    }, 
    "swupdate": {
        "lastinstall": "2019-06-28T12:26:48", 
        "state": "noupdates"
    }, 
    "swversion": "6.1.1.27575", 
    "type": "ZLLPresence", 
    "uniqueid": "00:17:88:01:04:b7:75:2e-02-0406"
}
```

```json
{
    "capabilities": {
        "certified": true, 
        "primary": false
    }, 
    "config": {
        "alert": "none", 
        "battery": 100, 
        "ledindication": false, 
        "on": true, 
        "pending": [], 
        "reachable": true, 
        "usertest": false
    }, 
    "manufacturername": "Philips", 
    "modelid": "SML001", 
    "name": "Hue temperature sensor 2", 
    "productname": "Hue temperature sensor", 
    "state": {
        "lastupdated": "2019-07-18T05:29:19", 
        "temperature": 2269
    }, 
    "swupdate": {
        "lastinstall": "2019-06-28T12:26:48", 
        "state": "noupdates"
    }, 
    "swversion": "6.1.1.27575", 
    "type": "ZLLTemperature", 
    "uniqueid": "00:17:88:01:04:b7:75:2e-02-0402"
}

```


```json
{
    "capabilities": {
        "certified": true, 
        "primary": false
    }, 
    "config": {
        "alert": "none", 
        "battery": 100, 
        "ledindication": false, 
        "on": true, 
        "pending": [], 
        "reachable": true, 
        "tholddark": 65534, 
        "tholdoffset": 7000, 
        "usertest": false
    }, 
    "manufacturername": "Philips", 
    "modelid": "SML001", 
    "name": "Hue ambient light sensor 2", 
    "productname": "Hue ambient light sensor", 
    "state": {
        "dark": true, 
        "daylight": false, 
        "lastupdated": "2019-07-18T05:28:44", 
        "lightlevel": 11215
    }, 
    "swupdate": {
        "lastinstall": "2019-06-28T12:26:48", 
        "state": "noupdates"
    }, 
    "swversion": "6.1.1.27575", 
    "type": "ZLLLightLevel", 
    "uniqueid": "00:17:88:01:04:b7:75:2e-02-0400"
}

```

### Dimmer switch
```json
{
    "config": {
        "on": true, 
        "reachable": true
    }, 
    "manufacturername": "Philips", 
    "modelid": "PHWA01", 
    "name": "Dimmer Switch 6 SceneCycle", 
    "recycle": true, 
    "state": {
        "lastupdated": "2019-07-17T20:20:49", 
        "status": 0
    }, 
    "swversion": "1.0", 
    "type": "CLIPGenericStatus", 
    "uniqueid": "WA0001"
}

{
    "capabilities": {
        "certified": true, 
        "inputs": [
            {
                "events": [
                    {
                        "buttonevent": 1000, 
                        "eventtype": "initial_press"
                    }, 
                    {
                        "buttonevent": 1001, 
                        "eventtype": "repeat"
                    }, 
                    {
                        "buttonevent": 1002, 
                        "eventtype": "short_release"
                    }, 
                    {
                        "buttonevent": 1003, 
                        "eventtype": "long_release"
                    }
                ], 
                "repeatintervals": [
                    800
                ]
            }, 
            {
                "events": [
                    {
                        "buttonevent": 2000, 
                        "eventtype": "initial_press"
                    }, 
                    {
                        "buttonevent": 2001, 
                        "eventtype": "repeat"
                    }, 
                    {
                        "buttonevent": 2002, 
                        "eventtype": "short_release"
                    }, 
                    {
                        "buttonevent": 2003, 
                        "eventtype": "long_release"
                    }
                ], 
                "repeatintervals": [
                    800
                ]
            }, 
            {
                "events": [
                    {
                        "buttonevent": 3000, 
                        "eventtype": "initial_press"
                    }, 
                    {
                        "buttonevent": 3001, 
                        "eventtype": "repeat"
                    }, 
                    {
                        "buttonevent": 3002, 
                        "eventtype": "short_release"
                    }, 
                    {
                        "buttonevent": 3003, 
                        "eventtype": "long_release"
                    }
                ], 
                "repeatintervals": [
                    800
                ]
            }, 
            {
                "events": [
                    {
                        "buttonevent": 4000, 
                        "eventtype": "initial_press"
                    }, 
                    {
                        "buttonevent": 4001, 
                        "eventtype": "repeat"
                    }, 
                    {
                        "buttonevent": 4002, 
                        "eventtype": "short_release"
                    }, 
                    {
                        "buttonevent": 4003, 
                        "eventtype": "long_release"
                    }
                ], 
                "repeatintervals": [
                    800
                ]
            }
        ], 
        "primary": true
    }, 
    "config": {
        "battery": 100, 
        "on": true, 
        "pending": [], 
        "reachable": true
    }, 
    "diversityid": "73bbabea-3420-499a-9856-46bf437e119b", 
    "manufacturername": "Philips", 
    "modelid": "RWL021", 
    "name": "Wohnzimmer Schalter", 
    "productname": "Hue dimmer switch", 
    "state": {
        "buttonevent": 1002, 
        "lastupdated": "2019-07-17T20:20:39"
    }, 
    "swupdate": {
        "lastinstall": "2019-06-14T11:38:41", 
        "state": "noupdates"
    }, 
    "swversion": "5.45.1.17846", 
    "type": "ZLLSwitch", 
    "uniqueid": "00:17:88:01:06:72:43:bd-02-fc00"
}

```

### Unknown until now
```json
{
    "config": {
        "on": true, 
        "reachable": true
    }, 
    "manufacturername": "Philips", 
    "modelid": "PHA_STATE", 
    "name": "MotionSensor 11.Companion", 
    "recycle": true, 
    "state": {
        "lastupdated": "2019-07-18T05:12:11", 
        "status": 0
    }, 
    "swversion": "1.0", 
    "type": "CLIPGenericStatus", 
    "uniqueid": "MotionSensor 11.Companion"
}

```


```json
{
    "config": {
        "configured": false, 
        "on": true, 
        "sunriseoffset": 30, 
        "sunsetoffset": -30
    }, 
    "manufacturername": "Philips", 
    "modelid": "PHDL00", 
    "name": "Daylight", 
    "state": {
        "daylight": null, 
        "lastupdated": "none"
    }, 
    "swversion": "1.0", 
    "type": "Daylight"
}
```


```json
{
    "config": {
        "on": true, 
        "reachable": true
    }, 
    "manufacturername": "Philips", 
    "modelid": "WAKEUP", 
    "name": "Sensor for wakeup", 
    "recycle": true, 
    "state": {
        "flag": false, 
        "lastupdated": "2019-06-28T04:30:00"
    }, 
    "swversion": "A_1932073040", 
    "type": "CLIPGenericFlag", 
    "uniqueid": "L_04_jRdKq"
}
```


