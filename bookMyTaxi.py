# TODO: use this for web interface 
from typing import Any, Dict, NamedTuple

class CurrentUserInfo(NamedTuple):
    userType:Dict[int,int]
    userInfo:Dict[str, Any]
    error: int