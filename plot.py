#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
from datetime import datetime
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Database import *

db = Database()

sensorvalues = db.get_all()
sensors = db.get_sensors()

measurements = {}
print sensors
ids = []
for sensor in sensors:
    ids.append(sensor.uniqueid)

daynames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# no more expensive dicts, too much for the rpi
myvals = np.zeros((7,24,len(ids)), np.float64)
for sv in sensorvalues:
    if sv.motion:
        myvals[sv.dtime.weekday(),sv.dtime.hour,ids.index(sv.idsensor)] += 1.

"""
for day in range(myvals.shape[0]):
    for sensor in range(len(ids)):
        myvals[day,:,sensor] /= np.sum(myvals[day,:,sensor])
"""

       
"""
for sv in sensorvalues:
    if sv.idsensor not in measurements.keys():
        measurements[sv.idsensor] = {}
        measurements[sv.idsensor]["dtime"] = []
        measurements[sv.idsensor]["hours"] = []
        measurements[sv.idsensor]["weekdays"] = []
        measurements[sv.idsensor]["temp"] = []
        measurements[sv.idsensor]["light"] = []
        measurements[sv.idsensor]["motion"] = []

    measurements[sv.idsensor]["dtime"].append(sv.dtime)
    measurements[sv.idsensor]["hours"].append(sv.dtime.hour)
    measurements[sv.idsensor]["weekdays"].append(sv.dtime.weekday())
    
    #measurements[sv.idsensor]["temp"].append(sv.temperature)
    #measurements[sv.idsensor]["light"].append(sv.lightlevel)
    measurements[sv.idsensor]["motion"].append(sv.motion)
"""
sensovalues=None
print("all sensorvalues read from db")

##### MOTION HEATMAP PER DAY AND HOUR
# create an array that holds the weekday in the row, the hour in the column,
# and the count of motion-events as value
for idsensor in ids:
    fig = plt.figure()
    for s in sensors:
        if idsensor == s.uniqueid:
            name = s.name
    plt.suptitle(name)

    sns.heatmap(myvals[:,:,ids.index(idsensor)], cmap='Greens', annot=True)
    plt.xticks(np.array(range(24))+0.5, rotation = 0)
    plt.yticks(np.array(range(len(daynames)))+0.5, daynames, rotation=0)

plt.show()
system.exit(0)

##### GRAPHS OF ALL SENSORS
fig = plt.figure()
for idx,(idsensor,mlists) in enumerate(measurements.iteritems()):
    larr = np.array(mlists["dtime"])
    for s in sensors:
        if idsensor == s.uniqueid:
            name = s.name
    plt.suptitle(name)

    ax = fig.add_subplot(131)
    plt.title("temp")
    plt.plot(larr, np.array(mlists["temp"]), label=name)
    plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
    plt.ylim((0,40))
    plt.legend()

    ax = fig.add_subplot(132)
    plt.title("light")
    plt.plot(larr, np.array(mlists["light"]), label=name)
    plt.setp(ax.get_xticklabels(), ha="right", rotation=45) 
    plt.legend()

    ax = fig.add_subplot(133)
    plt.title("motion")
    plt.plot(larr, np.array(mlists["motion"])*(idx+1), 'x', label=name)
    plt.ylim((0.5,3.5))
    plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
    plt.legend()

plt.show()   
