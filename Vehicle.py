from abc import ABC, abstractmethod
from Common import Common

class Vehicle(Common, ABC):
    def __init__(self, id, reg_num, type, rental_fee):
        self.reg_num = reg_num
        self.type = type
        self.rental_fee = rental_fee
        super().__init__(id)

