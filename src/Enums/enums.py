from enum import Enum


class UserType(Enum):
    GUEST  = 0
    RIDER  = 1
    DRIVER = 2
    
    
class VehicleType(Enum):
    UNKNOWN = 0
    GO      = 1
    SEDAN   = 2
    SUV     = 3
   
class BookingType(Enum):
    DEFAULT    = 0
    INTER_CITY = 1
    INTRA_CITY = 2
    CAR_POOL   = 3
    PRE_BOOKED = 5
