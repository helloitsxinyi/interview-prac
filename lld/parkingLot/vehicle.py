from enum import Enum


class VehicleSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    XLARGE = 3


class Vehicle:
    def __init__(self, type: VehicleSize, licenseNumber: str):
        self.type = type
        self.licenseNumber = licenseNumber
