#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
from datetime import datetime
import sqlite3

class Sensor:
    def __init__(self, name, id_motion, id_temp, id_light):
        self.name = name
        self.id_motion = id_motion
        self.id_temp = id_temp
        self.id_light = id_light

        self.temperature = -1
        self.lightlevel = -1
        self.motion = False

        self.conn = None

class Hue:
    def __init__(self):
        self.hue_host = "XXX.XXX.XXX.XXX"
        self.hue_user = "XXXXXXXXXXXX"
        self.update_interval = 2

        # TODO: is there a way to link temp and light sensors automatically based on some ID?
        # TODO: put in external config
        self.sensors = []
        self.sensors.append(Sensor(name=u"Küche", id_motion=u"Küche Sensor", id_temp=u'Hue temperature sensor 3', id_light=u'Hue ambient light sensor 3'))
        self.sensors.append(Sensor(name=u"PrivFlur", id_motion=u"PrivFlur Sensor", id_temp=u'Hue temperature sensor 1', id_light=u'Hue ambient light sensor 1'))
        self.sensors.append(Sensor(name=u"Garderobe", id_motion=u"Garderobe Sensor", id_temp=u'Hue temperature sensor 2', id_light=u'Hue ambient light sensor 2'))

        self.check_and_create_db()

    def run(self):
        while True:
            self.update_data()
            time.sleep(self.update_interval)


    def check_and_create_db(self):
        self.conn = sqlite3.connect('hue.db')
        self.c = self.conn.cursor() 

        try:
            self.c.execute('''CREATE TABLE SENSORS
                         ([id] INTEGER PRIMARY KEY,[name] text, [motion] integer, [temperature] real, [lightlevel] integer, [Date] date)''')

            self.conn.commit()
        except Exception as e: # table already exists. TODO: improve check
            pass


    def update_data(self, store=True):
        r = requests.get(url="http://" + self.hue_host + "/api/" + self.hue_user + "/sensors")
        j = r.json()
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        for key in j.items():
            #print(json.dumps(key[1], indent=4, sort_keys=True))
            for s in self.sensors:
                if key[1]['name'] == s.id_motion:
                    s.motion = key[1]['state']['presence']
                elif key[1]['name'] == s.id_temp:
                    s.temperature = key[1]['state']['temperature']/100.0
                elif key[1]['name'] == s.id_light:
                    s.lightlevel = key[1]['state']['lightlevel'] 

        for s in self.sensors:
            print("%s: temp: %.2f, light: %d, motion: %d" % (s.name, s.temperature, s.lightlevel, s.motion))
            date = datetime.now() # TODO: use datetime from sensor instead of local?
            self.c.execute('''INSERT INTO SENSORS (name, motion, temperature, lightlevel, Date) VALUES (?,?,?,?,?)''', (s.name, s.motion, s.temperature, s.lightlevel,date))
            self.conn.commit()
        print("---")

     
if __name__ == "__main__":
    h = Hue()
    h.update_data()
    h.run()
