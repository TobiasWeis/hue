#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
from datetime import datetime
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('hue.db')
c = conn.cursor() 

c.execute('''SELECT * FROM SENSORS''')

rows = c.fetchall()

measurements = {}
measurements[u"Küche"] = [[],[],[],[]]
measurements[u"Garderobe"] = [[],[],[],[]]
measurements[u"PrivFlur"] = [[],[],[],[]]

for r in rows:
    for mk in measurements.keys():
        if r[1] == mk:
            measurements[mk][0].append(datetime.strptime(r[5], '%Y-%m-%d %H:%M:%S.%f'))
            measurements[mk][1].append(r[2])
            measurements[mk][2].append(r[3])
            measurements[mk][3].append(r[4])
        #print r

for i in [1,2,3]:
    for k,v in measurements.items():
        larr = np.array(v[0]) # dates
        varr = np.array(v[i]) # values
        fig,ax = plt.subplots()
        plt.title(k)
        plt.plot(larr, varr)
        plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
plt.show()
