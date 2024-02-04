from tyre.tyre import Tyre

class CarriganTyres(Tyre):
  def __init__(self, sensor_values):
    self.sensor_values = sensor_values

  def needs_service(self):
    return any(value >= 0.9 for value in self.sensor_values)