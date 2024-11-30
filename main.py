from Car import Car
from Rental import Rental
from Truck import Truck
import datetime

class CarRentalSystem:
    def __get_vehicle_by_id(self, id):
        for car in self.cars:
            print(id, " ", car.id)
            if car.id == id: print("its a match1")
            if car.id == id: return car

        return None

    def __is_vehicle_rentable(self, vehicle_id, date):
        vehicle = self.__get_vehicle_by_id(vehicle_id)
        print(vehicle)

        if vehicle is None: raise ValueError(f"Nincs ilyen azonosítójú jármű a rendszerben: {vehicle_id} ")

        for rental in self.rentals:
            if vehicle.id == vehicle_id and rental.day == date: return False

        return True

    def rent_a_car(self):
        for car in self.cars:
            print(f"{car.id} {car.type}")

        while True:
            try:
                car_id_entered = int(input("Melyik autót kívánja bérbe adni?"))
            except ValueError as e:
                print(f"Érvénytelen adat: {e}")
                continue

            car_to_rent = self.__get_vehicle_by_id(car_id_entered)
            if car_to_rent is None:
                print(f"A megadott jármű nem található")
                continue

            try:
                date_entered = input("Melyik napra kívánja bérbe adni a járművet? (éééé-hh-nn) ")
                datetime.datetime.strptime(date_entered, "%Y-%m-%d")
            except ValueError as e:
                print(e)

            print(date_entered)

    def list_rentals(self):
        for rental in self.rentals:
            print(rental.id, " - ", rental.car.type, " - ", rental.day)

    def cancel_rental(self):
        self.list_rentals()
        while True:
            try:
                car_id_entered = int(input("Melyik bérlést kívánja lemondani?"))
            except ValueError as e:
                print(f"Érvénytelen adat: {e}")
                continue
        pass

    def print_options(self):
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("X. Kilépés")

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

        while True:
            self.print_options()
            option = input("Kérem, válasszon:")
            match option:
                case "1":
                    self.rent_a_car()
                case "2":
                    self.cancel_rental()
                case "3":
                    self.list_rentals()
                case "x":
                    break
                case _:
                    print("Ez az opció nem választható")


car_rental_system = CarRentalSystem()
