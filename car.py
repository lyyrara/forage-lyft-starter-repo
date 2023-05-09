from abc import ABC, abstractmethod
from engine.engine import Engine

class Car(ABC):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    @abstractmethod
    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()
