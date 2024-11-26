from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, id, reg_num, type, rental_fee):
        super().__init__(id, reg_num, type, rental_fee)
        print("I am a car")
