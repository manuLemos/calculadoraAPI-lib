from pydantic import BaseModel


class OperationRequest(BaseModel):

    a: float
    b: float

class OperationRequest2(BaseModel):

    a: float


class OperationResponse(BaseModel):

    result: float
