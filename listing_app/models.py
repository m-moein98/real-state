from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from fastapi import Query


class Listing(BaseModel):
    # todo: updatedAt should be only updated after update and cratedAt should not change each time
    ownerId: str
    type: str = Query(..., regex="^(HOUSE|APARTMENT)$")
    availableNow: Optional[bool] = True
    address: dict = {
        "streetName": "",
        "streetNumber": "",
        "district": "",
        "city": ""
    }
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()


class Createlisting(BaseModel):
    # todo: type regex should appear in the openAPI docuement
    type: str = Query(..., regex="^(HOUSE|APARTMENT)$")
    availableNow: Optional[bool] = True
    address: dict = {
        "streetName": "",
        "streetNumber": "",
        "district": "",
        "city": ""
    }
