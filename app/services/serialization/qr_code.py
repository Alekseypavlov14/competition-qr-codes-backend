from models.qr_code import QRCode

def get_qr_code_dict(qr_code: QRCode):
  return ({
    "id": qr_code.id,
    "user_id": qr_code.user_id,
    "content": qr_code.content,
    "hash": qr_code.hash,
    "scans": qr_code.scans,
  })
