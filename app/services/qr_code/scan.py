from pydantic import BaseModel

class ScanJSON(BaseModel):
  hash: str
  date: str
