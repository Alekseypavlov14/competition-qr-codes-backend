from pydantic import BaseModel

class ScanJSON(BaseModel):
  qr_code_id: int
  date: str
