from abc import ABC, abstractmethod

# abstract class for smth
# object of this class cannot be created, must inherit your class from this one
class ABCAnimal(ABC):
    def __init__(self, name):
        self.name = name

   def set_weight(self, weight):
        self.weight = weight

   @abstractmethod
    def eat(self, food_amount):
        pass
