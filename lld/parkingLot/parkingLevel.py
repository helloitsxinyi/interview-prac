from abc import ABC, abstractmethod
from typing import Dict

from lld.parkingLot.parkingObservers import ParkingPublisher, ParkingSubscriber
from lld.parkingLot.parkingSpot import ParkingSpot


# parkingLevel is the publisher.
class ParkingLevel(ParkingPublisher):
    def __init__(self, level: int, capacity: int, parkingSpotsMap: Dict[int, ParkingSpot] = {}):
        # empty dict? or prefilled dict with spotnum as key and vals as None?
        self.level = level
        self.parkingSpotsMap = parkingSpotsMap
        self.subscribers: list[ParkingSubscriber] = []
        self.available = capacity

    def findAvailableSpot(self, vehicle):
        # for loop mb slow - can use O(1) lookup?
        for spot_num, spot in self.parkingSpotsMap.items():
            if not spot.isOccupied:
                return spot
        return None

    def get_number_spots_left(self):
        return sum(1 for spot in self.parkingSpotsMap.values() if not spot.isOccupied)

    def add_subscriber(self, subscriber:ParkingSubscriber):
        self.subscribers.append(subscriber)
        return

    def remove_subscriber(self, subscriber:ParkingSubscriber):
        self.subscribers.remove(subscriber)
        return

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.level, self.available, self.parkingSpotsMap)
        return


class DisplayParkingLevelStatus(ParkingSubscriber):
    def update(self, levelId: int, available_spots: int, parkingSpotsMap: Dict[int, ParkingSpot]):
        print(f'{available_spots} left on level {levelId}')
        print(f'Status is {parkingSpotsMap}')
        return