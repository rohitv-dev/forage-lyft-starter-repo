from abc import ABC, abstractmethod

class Battery(ABC):
  def __init__(self, current_date, last_service_date):
    self.current_date = current_date
    self.last_service_date = last_service_date

  @abstractmethod
  def needs_service(self):
    pass