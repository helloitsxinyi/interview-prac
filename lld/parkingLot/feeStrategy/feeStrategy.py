from abc import ABC, abstractmethod

from lld.parkingLot.parkingTicket import ParkingTicket


class FeeStrategy(ABC):
    @abstractmethod
    def calculateFee(self, ticket: ParkingTicket):
        pass
