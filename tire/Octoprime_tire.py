from tire.Tire import Tire



class OctoprimeTire(Tire):
    def __init__(self, sensor = None):
        self.sensor = sensor
        
        

    def need_serviced(self):
        if sum(self.sensor) >= 3:
                return True
        return False
