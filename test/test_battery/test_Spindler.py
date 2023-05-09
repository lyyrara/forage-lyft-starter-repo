import unittest
from battery.SpindlerBattery import SpindlerBattery
from datetime import datetime, timedelta


class Test_SpindlerBattery(unittest.TestCase):

    def test_need_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)


        battery = SpindlerBattery(last_service_date, current_date)

        self.assertTrue(battery.battery_should_be_serviced())


    def test_need_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)


        battery = SpindlerBattery(last_service_date, current_date)

        self.assertFalse(battery.battery_should_be_serviced())