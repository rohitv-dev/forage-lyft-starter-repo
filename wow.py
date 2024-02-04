from car_factory import CarFactory
from datetime import datetime

current_date = datetime.today().date()

car = CarFactory.create_calliope(current_date, current_date.replace(year=current_date.year - 1), 30000, 0)

print(car.needs_service())