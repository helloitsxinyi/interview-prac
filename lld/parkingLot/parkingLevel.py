from abc import ABC, abstractmethod
from typing import Dict

from lld.parkingLot.parkingObservers import ParkingSubject, ParkingObserver
from lld.parkingLot.parkingSpot import ParkingSpot


# parkingLevel is the publisher.
class ParkingLevel(ParkingSubject):
    def __init__(self, level: int, capacity: int, parkingSpotsMap: Dict[int, ParkingSpot] = {}):
        # empty dict? or prefilled dict with spotnum as key and vals as None?
        self.level = level
        self.parkingSpotsMap = parkingSpotsMap
        self.observers: list[ParkingObserver] = []
        self.available = capacity

    def findAvailableSpot(self, vehicle):
        # for loop mb slow - can use O(1) lookup?
        for spot_num, spot in self.parkingSpotsMap.items():
            if not spot.isOccupied and spot.canFitVehicle(vehicle):
                return spot
        return None

    def get_number_spots_left(self):
        return sum(1 for spot in self.parkingSpotsMap.values() if not spot.isOccupied)

    def add_observer(self, observer:ParkingObserver):
        self.observers.append(observer)
        return

    def remove_observer(self, observer:ParkingObserver):
        self.observers.remove(observer)
        return

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.level, self.available, self.parkingSpotsMap)
        return


class DisplayParkingLevelStatus(ParkingObserver):
    def update(self, levelId: int, available_spots: int, parkingSpotsMap: Dict[int, ParkingSpot]):
        print(f'{available_spots} left on level {levelId}')
        print(f'Status is {parkingSpotsMap}')
        return