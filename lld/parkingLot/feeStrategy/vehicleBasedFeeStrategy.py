from lld.parkingLot.feeStrategy.feeStrategy import FeeStrategy
from lld.parkingLot.parkingTicket import ParkingTicket
from lld.parkingLot.vehicle import VehicleSize


class VehicleBasedStrategy(FeeStrategy):
    def __init__(self):
        self.vehicle_rates = {VehicleSize.SMALL: 0.1,
                              VehicleSize.MEDIUM: 0.2,
                              VehicleSize.LARGE: 0.3,
                              VehicleSize.XLARGE: 0.4}

    def calculateFee(self, ticket: ParkingTicket):
        num_minutes = (ticket.exitTime - ticket.entryTime).minute
        vehicle_type = ticket.vehicle.type
        return self.vehicle_rates[vehicle_type] * num_minutes
