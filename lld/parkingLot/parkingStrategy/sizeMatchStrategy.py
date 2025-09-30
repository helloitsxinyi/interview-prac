from lld.parkingLot.parkingLevel import ParkingLevel
from lld.parkingLot.parkingStrategy.parkingStrategy import ParkingStrategy
from lld.parkingLot.vehicle import Vehicle


class SizeMatchStrategy(ParkingStrategy):
    def parkingStrategy(self, vehicle: Vehicle, parkingLevel: ParkingLevel):
        # need to handle how to find next avail spot if occupied but can't fit
        spot = parkingLevel.findAvailableSpot(vehicle)
        if spot.canFitVehicle(vehicle):
            spot.parkVehicle()
            return spot
        return None