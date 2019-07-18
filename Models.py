# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float

'''
the following lines are used for sqlalchemies ORM mapper,
the objects map directly to database tables
can these be put into an own class?
'''
Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    uniqueid = Column(String)
    name = Column(String)
    id_motion = Column(String)
    name_motion = Column(String)
    id_temp = Column(String)
    name_temp = Column(String)
    id_light = Column(String)
    name_light = Column(String)

    def __str__(self):
        ret = self.name + "\n"
        ret += "motion: ["+self.id_motion+"] " + self.name_motion + "\n"
        ret += "temp  : ["+self.id_temp+"] " + self.name_temp + "\n"
        ret += "light : ["+self.id_light+"] " + self.name_light + "\n"
        return ret

class SensorValue(Base):
    __tablename__ = 'sensorvalues'

    id = Column(Integer, primary_key=True)
    idsensor = Column(Integer)
    temperature = Column(Integer)
    lightlevel = Column(Integer)
    motion = Column(Integer)
    dtime = Column(DateTime)

    def __str__(self):
        ret = "idsensor: %s"%self.idsensor + ": "
        ret += "m:%d"%self.motion + ", "
        ret += "l:%.2f"%self.lightlevel + ", "
        ret += "t:%.2f"%self.temperature + "\n"
        ret += str(self.dtime)
        return ret
