from datetime import datetime
from dateutil import relativedelta
from battery.battery import Battery

class NubbinBattery(Battery):
  def __init__(self, current_date, last_service_date):
    super().__init__(current_date, last_service_date)

  def needs_service(self):
    delta = relativedelta.relativedelta(self.current_date, self.last_service_date)
    if delta.years >= 4:
      return True
    else:
      return False