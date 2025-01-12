from pydantic import BaseModel
from enums.general_status import Status

class storeRequest(BaseModel):
    currency_id: int
    label: str
    iban: str
    bank_name: str
    bank_account: str
    swift_number: str
    type: Status


class updateRequest(BaseModel):
    currency_id: int
    label: str
    iban: str
    bank_name: str
    bank_account: str
    swift_number: str
    type: Status