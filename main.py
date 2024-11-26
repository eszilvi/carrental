from Car import Car
from Rental import Rental
from Truck import Truck
from Vehicle import Vehicle
import datetime

class CarRentalSystem:

    def rent_a_car(self, car_id, day):
        pass

    def cancel_rental(self, rental_id):
        pass

    def list_rentals(self):
        for rental in self.rentals:
            print(rental.car.type, "aa")

    def print_options(self):
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")

    def __init__(self):
        print("a")
        self.cars = [
            Car(1, "HSH-746", "Toyota Avensis 1.8 Sol", 10000),
            Truck(2, "BXD-344", "Mercedes Vito", 8000),
            Car(3, "CKU-101", "Pontiac Trans AM GTA", 180000),
        ]

        self.rentals = [
            Rental(1, self.cars[0], datetime.date(2024, 12, 1)),
            Rental(2, self.cars[2], datetime.date(2024, 12, 3)),
            Rental(3, self.cars[1], datetime.date(2024, 12, 2)),
            Rental(4, self.cars[1], datetime.date(2024, 12, 3))
        ]

        list_re

car_rental_system = CarRentalSystem()
