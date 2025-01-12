from pydantic import BaseModel
from enums.general_status import Status

class storeRequest(BaseModel):
    name: str
    address: str
    asset_id: int
    network_id: int
    type: Status

class updateRequest(BaseModel):
    name: str
    address: str
    asset_id: int
    network_id: int
    type: Status

