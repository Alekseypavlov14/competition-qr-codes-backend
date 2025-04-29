from services.serialization.scan import get_scan_dict
from shared.utils.array import map
from models.qr_code import QRCode

def get_qr_code_dict(qr_code: QRCode):
  scans = map(qr_code.scans, get_scan_dict)

  return ({
    "id": qr_code.id,
    "user_id": qr_code.user_id,
    "content": qr_code.content,
    "hash": qr_code.hash,
    "scans": scans,
    "date": qr_code.date,
  })
