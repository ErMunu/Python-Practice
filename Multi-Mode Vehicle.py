from abc import ABC, abstractmethod

class IDrivable(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

class IFlyable(ABC):
    @abstractmethod
    def fly(self, distance):
        pass

class FlyingCar(IDrivable, IFlyable):
    # Implement drive and fly
    # drive speed = 100 km/h, fly speed = 300 km/h
    def drive(self, dist):
      return dist/100
    def fly(self, dist):
      return dist/300

car = FlyingCar()
X = int(input())
