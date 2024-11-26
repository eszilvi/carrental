from abc import ABC, abstractmethod

class Common(ABC):
    def __init__(self, id):
        self.id = id