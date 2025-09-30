from abc import ABC, abstractmethod
from typing import Dict

from lld.parkingLot.parkingSpot import ParkingSpot


class ParkingSubscriber(ABC):
    @abstractmethod
    def update(self, levelId: int, available: int, parkingSpotsMap: Dict[int, ParkingSpot]):
        pass

# implement ParkingSubject interface just in case we want to implement publishers for various groupings (eg across level, across whole carpark etc)
class ParkingPublisher(ABC):
    @abstractmethod
    def add_subscriber(self, observer:ParkingSubscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, observer:ParkingSubscriber):
        pass
    @abstractmethod
    def notify_subscribers(self):
        pass
