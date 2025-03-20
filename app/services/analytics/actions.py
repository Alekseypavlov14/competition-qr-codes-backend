from services.serialization.qr_code import get_qr_code_dict
from api.exceptions import NotFoundException
from models.qr_code import QRCode

def get_qr_code_analytics(qr_code_id):
  qr_code = QRCode.query.filter_by(id=qr_code_id).first()
  if not qr_code: raise NotFoundException

  qr_code_analytics = get_qr_code_dict(qr_code)
  return qr_code_analytics
