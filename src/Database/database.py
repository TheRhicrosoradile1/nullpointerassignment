import configparser
from pathlib import Path

from bookMyTaxi import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_bookMyTaxi.json"
)

def get_database_path(config_file: Path) -> Path:
    """Return the current path to the database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    """Create the database."""
    try:
        # TODO: change this to create if not existing instead
        db_path.write_text("[]")  # Empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
    

# ?? this should be better off a interface ??  
class StorageService :
    
    def saveRider(rider)->bool:
        pass
    
    def saveDriver( driver)->bool:
        pass
    
    def saveVehicle( vehicle)->bool:
        pass
    
    def updateLocation( vehicle)->bool:
        pass
    
    def book( booking)->bool:
        pass
    
    def find( lat,  lon,  maxDistance)->Vehicle:
        pass
    
    def rideHistory(riderUserId):
        pass
    
    def endTrip(timeStamp, bookingId)->bool:
        pass
    
    def deleteRider():
        pass
    
    def deleteDriver():
        pass
    
    def deleteVehicle():
        pass
    
    def deleteBooking():
        pass
    