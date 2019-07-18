#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
from datetime import datetime
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

from Database import *


db = Database()

sensorvalues = db.get_all()

measurements = {}

for sv in sensorvalues:
    if sv.idsensor not in measurements.keys():
        measurements[sv.idsensor] = {}
        measurements[sv.idsensor]["dtime"] = []
        measurements[sv.idsensor]["temp"] = []
        measurements[sv.idsensor]["light"] = []
        measurements[sv.idsensor]["motion"] = []

    measurements[sv.idsensor]["dtime"].append(sv.dtime)
    measurements[sv.idsensor]["temp"].append(sv.temperature)
    measurements[sv.idsensor]["light"].append(sv.lightlevel)
    measurements[sv.idsensor]["motion"].append(sv.motion)

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
