# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Models import * 

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///hue.db', echo=False)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_sensorvalue(self, sensorvalue):
        self.session.add(sensorvalue)
        self.session.commit()

    def get_sensors(self):
        return self.session.query(Sensor).order_by(Sensor.id)

    """
    arguments:
        sensors: list of Sensor objects
    """
    def add_sensors(self, sensors):
        for s in sensors:
            exists = self.session.query(Sensor).filter_by(uniqueid=s.uniqueid).first()
            if not exists:
                self.session.add(s)
                self.session.commit()

    def get_all(self):
        return self.session.query(SensorValue).order_by(SensorValue.id)


