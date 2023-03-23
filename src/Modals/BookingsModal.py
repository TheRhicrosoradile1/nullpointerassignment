class Booking:
    def __init__(self,bookingId,bookingName,bookingType,bookingTicket):
        self.bookingId   = bookingId
        self.bookingName = bookingName
        self.bookingType = bookingType
        self.bookingTicket = bookingTicket
     


class RideHistory:
    def __init__(self):
        pass
    # TODO: implement this as needed
   
   
class Ticket:
    def __init__(self,startTime,endTime,route,driverId,requesterId) -> None:
        # ?? should route be a diffrent class here ??
        self.startTime=startTime
        self.endTime=endTime
        self.route=route
        self.requesterId=requesterId
        self.driverId=driverId