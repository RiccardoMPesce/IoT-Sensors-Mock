from pydantic import BaseModel

class ErrorResponse(BaseModel):
    """
    Erros reponses Model
    """

    detail: str
    status_code: int

    class Config:
        schema_extra = {
            "example": {
                "detail": "MongoDb not ready",
                "status_code": 406,
            }
        }
