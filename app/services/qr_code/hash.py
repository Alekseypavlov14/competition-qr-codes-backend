from shared.utils.string import generate_random_string_by_length
from api.exceptions import NotFoundException
from shared.const import hash_length
from models.qr_code import QRCode

def generate_unique_hash():
  return generate_random_string_by_length(hash_length)

def get_qr_code_by_hash(hash: str):
  qr_code = QRCode.query.filter_by(hash=hash)
  if not qr_code: raise NotFoundException

  return qr_code