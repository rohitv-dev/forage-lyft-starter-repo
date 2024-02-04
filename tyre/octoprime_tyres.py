from tyre.tyre import Tyre

class OctoprimeTyres(Tyre):
  def __init__(self, sensor_values):
    self.sensor_values = sensor_values

  def needs_service(self):
    return sum(self.sensor_values) >= 3