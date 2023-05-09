import unittest
from engine.willoughby_engine import WilloughbyEngine



class Test_WilloughbyEngine(unittest.TestCase):

    def test_need_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage) 

        self.assertTrue(engine.engine_should_be_serviced())


    def test_need_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage) 


        self.assertFalse(engine.engine_should_be_serviced())