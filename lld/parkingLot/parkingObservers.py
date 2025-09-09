from abc import ABC, abstractmethod
from typing import Dict

from lld.parkingLot.parkingSpot import ParkingSpot


class ParkingObserver(ABC):
    @abstractmethod
    def update(self, levelId: int, available: int, parkingSpotsMap: Dict[int, ParkingSpot]):
        pass

# implement ParkingSubject interface just in case we want to implement publishers for various groupings (eg across level, across whole carpark etc)
class ParkingSubject(ABC):
    @abstractmethod
    def add_observer(self, observer:ParkingObserver):
        pass

    def remove_observer(self, observer:ParkingObserver):
        pass

    def notify_observers(self):
        pass
