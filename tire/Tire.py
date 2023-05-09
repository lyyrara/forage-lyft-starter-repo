from abc import ABC, abstractmethod
from datetime import datetime

class Battery():
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        pass