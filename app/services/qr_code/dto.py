from pydantic import BaseModel

class QRCodeDTO(BaseModel):
  content: str
