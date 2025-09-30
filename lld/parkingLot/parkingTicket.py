import datetime
import uuid

from lld.parkingLot.parkingSpot import ParkingSpot
from lld.parkingLot.vehicle import Vehicle


class ParkingTicket:
    def __init__(self, spot: ParkingSpot, vehicle: Vehicle):
        self.ticketId = uuid.uuid4()
        self.spot = spot
        self.entryTime = datetime.datetime.now()
        self.exitTime = None
        self.vehicle = vehicle

    def set_exitTime(self):
        self.exitTime = datetime.datetime.now()
        return
