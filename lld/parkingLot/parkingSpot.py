from parkingLot.vehicle import Vehicle, VehicleSize


class ParkingSpot:
    def __init__(self, spotNumber: int, isOccupied: bool, occupant: Vehicle, size: VehicleSize, level: int):
        self.spotNumber = spotNumber
        self.isOccupied = isOccupied
        self.occupant = occupant
        self.size = size
        self.level = level

    def getIsOccupied(self):
        if self.isOccupied:
            return False
        return True

    def parkVehicle(self, vehicle):
        if self.canFitVehicle(vehicle):
            self.occupant = vehicle
            self.isOccupied = True
        return

    def unparkVehicle(self):
        self.isOccupied = False
        self.occupant = None
        return

    def canFitVehicle(self, vehicle):
        if vehicle.type <= self.size:
            return True
        return False
