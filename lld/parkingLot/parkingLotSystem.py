# like navigator for strategy
from lld.parkingLot.feeStrategy.feeStrategy import FeeStrategy
from lld.parkingLot.feeStrategy.flatFeeStrategy import FlatFeeStrategy
from lld.parkingLot.parkingLevel import ParkingLevel
from lld.parkingLot.parkingSpot import ParkingSpot
from lld.parkingLot.parkingStrategy.nearestParkingStrategy import SizeMatchStrategy

from lld.parkingLot.parkingStrategy.parkingStrategy import ParkingStrategy
from lld.parkingLot.parkingTicket import ParkingTicket
from lld.parkingLot.vehicle import Vehicle


# want to include ParkingSubscriber to track all floors?
class ParkingLotSystem:
    def __init__(self):
        # need to pass in params for ParkingLevel?
        self.levels = list[ParkingLevel] = []
        self.feeStrategy = FlatFeeStrategy()
        self.parkingStrategy = SizeMatchStrategy()


    def set_fee_strategy(self, feeStrategy: FeeStrategy):
        self.feeStrategy = feeStrategy
        return

    def set_parking_strategy(self, parkingStrategy: ParkingStrategy):
        self.parkingStrategy = parkingStrategy
        return

    def park_vehicle(self, vehicle: Vehicle):
        parkingSpot = self.parkingStrategy(vehicle)
        parkingSpot.parkVehicle(vehicle)
        ticket = ParkingTicket(parkingSpot, vehicle)
        return ticket

    def unpark_vehicle(self, ticket: ParkingTicket, parkingSpot: ParkingSpot):
        # side effects??
        parkingSpot.unparkVehicle()
        ticket.set_exitTime()
        return

