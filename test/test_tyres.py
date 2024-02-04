import unittest
from decimal import Decimal

from tyre.carrigan_tyres import CarriganTyres
from tyre.octoprime_tyres import OctoprimeTyres

class TestCarriganTyres(unittest.TestCase):
  def test_engine_should_be_serviced(self):
    sensor_values = [Decimal(0.2), Decimal(0.4), Decimal(0.1), Decimal(0.9)] 
    tyres = CarriganTyres(sensor_values)

    self.assertTrue(tyres.needs_service())

  def test_engine_should_not_be_serviced(self):
    sensor_values = [Decimal(0.2), Decimal(0.4), Decimal(0.1), Decimal(0.8)] 
    tyres = CarriganTyres(sensor_values)

    self.assertFalse(tyres.needs_service())

class TestOctoprimeTyres(unittest.TestCase):
  def test_engine_should_be_serviced(self):
    sensor_values = [Decimal(0.6), Decimal(0.7), Decimal(0.8), Decimal(0.9)] 
    tyres = OctoprimeTyres(sensor_values)

    self.assertTrue(tyres.needs_service())

  def test_engine_should_not_be_serviced(self):
    sensor_values = [Decimal(0.2), Decimal(0.4), Decimal(0.1), Decimal(0.8)] 
    tyres = OctoprimeTyres(sensor_values)

    self.assertFalse(tyres.needs_service())

if __name__ == "__main__":
  unittest.main()