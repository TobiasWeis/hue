#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
TODOs:
    * put values in config
    * cleanup messy redundant code
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import requests
import time
from datetime import datetime
import sqlite3

from Models import Sensor, SensorValue
from Database import *

class Hue:
    def __init__(self):
        self.database = Database()
        self.hue_host = "192.168.178.34"
        self.hue_user = "Lg3nA6dfY05UaO4WcbVFLCljr4Yi7KQtSqtCxGY4"
        self.update_interval = 2

        self.sensors = self.populate_sensors()
        self.database.add_sensors(self.sensors)
        self.sensors = self.database.get_sensors()

    """
    we already know that a hue motion sensor has three different sensors in 
    the response that share the first part of the unique id
    """
    def populate_sensors(self):
        r = requests.get(url="http://" + self.hue_host + "/api/" + self.hue_user + "/sensors")
        j = r.json()
        sensors = {}
        for key in j.items():

            if key[1]['type'] == "ZLLPresence":
                sensorid = "".join(key[1]['uniqueid'].split("-")[:-1])
                if sensorid not in sensors.keys():
                    sensors[sensorid] = Sensor(
                            uniqueid=sensorid,
                            name=key[1]['name'].decode('utf8'), 
                            name_motion=key[1]['name'].decode('utf8'),
                            id_motion=key[1]['uniqueid'])
                else:
                    sensors[sensorid].id_motion = key[1]['uniqueid']
                    sensors[sensorid].name_motion = key[1]['name'].decode('utf8')
                    sensors[sensorid].name = key[1]['name'].decode('utf8')
            elif key[1]['type'] == "ZLLTemperature":
                sensorid = "".join(key[1]['uniqueid'].split("-")[:-1])
                if sensorid not in sensors.keys():
                    sensors[sensorid] = Sensor(
                            uniqueid=sensorid,
                            id_temp=key[1]['uniqueid'], 
                            name_temp=key[1]['name'].decode('utf8'))
                else:
                    sensors[sensorid].name_temp = key[1]['name']
                    sensors[sensorid].id_temp = key[1]['uniqueid']
            elif key[1]['type'] == "ZLLLightLevel":
                sensorid = "".join(key[1]['uniqueid'].split("-")[:-1])
                if sensorid not in sensors.keys():
                    sensors[sensorid] = Sensor(
                            uniqueid=sensorid,
                            name_light=key[1]['name'].decode('utf8'),
                            id_light=key[1]['uniqueid']
                            )
                else:
                    sensors[sensorid].name_light = key[1]['name'].decode('utf8')
                    sensors[sensorid].id_light = key[1]['uniqueid']

        print "Found the following sensors: "
        retsensors = []
        for s,v in sensors.iteritems():
            retsensors.append(v)
            print s,":",v

        return retsensors

    def run(self):
        while True:
            self.update_data()
            time.sleep(self.update_interval)

    def update_data(self, store=True):
        r = requests.get(url="http://" + self.hue_host + "/api/" + self.hue_user + "/sensors")
        j = r.json()

        sensorvalues = {}
        for key in j.items():
            try:
                sid = key[1]['uniqueid']
            except:
                continue

            for s in self.sensors:
                if sid == s.id_motion:
                    if s.uniqueid not in sensorvalues.keys():
                        sensorvalues[s.uniqueid] = SensorValue()
                    sensorvalues[s.uniqueid].idsensor = s.uniqueid
                    sensorvalues[s.uniqueid].motion = key[1]['state']['presence']

                if sid == s.id_temp:
                    if s.uniqueid not in sensorvalues.keys():
                        sensorvalues[s.uniqueid] = SensorValue()
                    sensorvalues[s.uniqueid].idsensor = s.uniqueid
                    sensorvalues[s.uniqueid].temperature = key[1]['state']['temperature']/100.0

                if sid == s.id_light:
                    if s.uniqueid not in sensorvalues.keys():
                        sensorvalues[s.uniqueid] = SensorValue()
                    sensorvalues[s.uniqueid].idsensor = s.uniqueid
                    sensorvalues[s.uniqueid].lightlevel = key[1]['state']['lightlevel']

        for k,s in sensorvalues.iteritems():
            s.dtime = datetime.now()
            self.database.add_sensorvalue(s)

        # only for test: query all values in db
        if False:
            print "------------ From DB:"
            for instance in self.database.session.query(SensorValue).order_by(SensorValue.id):
                print(instance)
            print("---")

     
if __name__ == "__main__":
    h = Hue()
    #h.update_data()
    h.run()
