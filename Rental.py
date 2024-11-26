from Common import Common

class Rental(Common):
    def __init__(self, id, car, day):
        super().__init__(id)
        self.car = car
        self.day = day

