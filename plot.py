#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
from datetime import datetime
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

from Sensor import *
from Database import *


db = Database()

sensorvalues = db.get_all()

measurements = {}

for sv in sensorvalues:
    if sv.name not in measurements.keys():
        measurements[sv.name] = {}
        measurements[sv.name]["dtime"] = []
        measurements[sv.name]["temp"] = []
        measurements[sv.name]["light"] = []
        measurements[sv.name]["motion"] = []

    measurements[sv.name]["dtime"].append(sv.dtime)
    measurements[sv.name]["temp"].append(sv.temperature)
    measurements[sv.name]["light"].append(sv.lightlevel)
    measurements[sv.name]["motion"].append(sv.motion)

fig = plt.figure()

for idx,(name,mlists) in enumerate(measurements.iteritems()):
    larr = np.array(mlists["dtime"])
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
