from Vehicle import Vehicle

# Concrete class - Truck
class Truck(Vehicle):
    def __init__(self, id, reg_num, type, rental_fee):
        super().__init__(id, reg_num, type, rental_fee)
