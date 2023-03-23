class Ticket:
    def __init__(self,startTime,endTime,route,driverId,requesterId) -> None:
        # ?? should route be a diffrent class here ??
        self.startTime=startTime
        self.endTime=endTime
        self.route=route
        self.requesterId=requesterId
        self.driverId=driverId
     