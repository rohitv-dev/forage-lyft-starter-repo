from abc import ABC
from datetime import datetime
from dateutil import relativedelta
from battery.battery import Battery

class SpindlerBattery(Battery, ABC):
  def __init__(self, last_service_date):
    super().__init__(last_service_date)

  def needs_service(self):
    current_date = datetime.today().date()
    delta = relativedelta.relativedelta(current_date, self.last_service_date)
    if delta.years >= 2:
      return True
    else:
      return False