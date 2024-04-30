from pydantic import BaseModel, ValidationError, constr
from typing import List

# Define a Pydantic model for the incoming message
class Message(BaseModel):
    message: constr(max_length=1000)

# Define a Pydantic model for the model response
class ModelResponse(BaseModel):
    label: str
    confidences: List[dict]
