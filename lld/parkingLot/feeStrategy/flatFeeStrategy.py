from lld.parkingLot.feeStrategy.feeStrategy import FeeStrategy
from lld.parkingLot.parkingTicket import ParkingTicket


class FlatFeeStrategy(FeeStrategy):
    def __init__(self):
        self.flatFee = 5.00

    def calculateFee(self, parkingTicket: ParkingTicket):
        return self.flatFee

