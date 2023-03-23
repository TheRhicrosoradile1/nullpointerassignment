class UserInfo:
    MAX_USER_RATING = 5
    MIN_USER_RATING = 0
    def __init__(self,username,id,password,phone,email,type=UserType.GUEST):
        self.username = username
        self.password = password
        self.type = type
        self.phone = phone
        self.email = email
        self.id = id
        
                 
class Rider(UserInfo):
    super().__inti__(self,username,id,password,phone,email,type=UserType.RIDER,riderRideHistory=[])
    self.riderRideHistory=riderRideHistory
    
    
    
    
class Driver(UserInfo):
        super().__inti__(self,username,id,password,phone,email,type=UserType.DRIVER,driverRideHistory=[])
        self.driverRideHistory=driverRideHistory
        
        
  