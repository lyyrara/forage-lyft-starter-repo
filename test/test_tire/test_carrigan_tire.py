import unittest
from tire.Carrigan_tire import CarriganTire



class Test_carrigan_tires(unittest.TestCase):

    def test_need_service_true(self):
        tire_wear = [0.1, 0.3, 0.2, 0.9]
        tire = CarriganTire(tire_wear)

        self.assertTrue(tire.need_serviced())


    def test_need_service_false(self):
        tire_wear = [0.1, 0.3, 0.2, 0.5]
        tire = CarriganTire(tire_wear)

        self.assertFalse(tire.need_serviced())