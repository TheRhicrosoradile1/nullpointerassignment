class VehicleHealth:
    # TODO: additional feature class that could enhance user experience
    pass
class Vehicle:
    MAX_CAR_RATING = 5
    MIN_CAR_RATING = 0
    
    # ?? should i store location object seperatly instead of lat,lng here ??
    def __init__(self,vehicleNumber,driverId,currRating,lat,lng,):
        self.vehicleNumber = vehicleNumber
        self.driverId = driverId
        self.currRating = currRating
        self.lat=lat
        self.lng=lng
        self.isAvaliable=True
