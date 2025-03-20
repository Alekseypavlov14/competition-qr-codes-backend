# libs
from pydantic import ValidationError
from flask import Blueprint, request

# services
from services.auth.middlewares import auth_required
from services.qr_code.dto import QRCodeDTO
from services.qr_code.scan import ScanJSON
from services.qr_code.qr_code import get_qr_code_dict
from services.qr_code.actions import create_qr_code, scan_qr_code

# shared
from shared.utils.datetime import get_time_from_iso
from api.exceptions import BadRequestException
from api.exceptions import BadRequestException

router = Blueprint('qr_codes', __name__, url_prefix='/qr-codes')

@auth_required
@router.post('/create')
def create():
  try:
    body = request.json
    qr_code_dto = QRCodeDTO(**body)

    qr_code = create_qr_code(qr_code_dto.content)
    qr_code_dict = get_qr_code_dict(qr_code)

    return qr_code_dict

  except ValidationError:
    raise BadRequestException
  
@auth_required
@router.post('/scan')
def scan():
  try: 
    body = request.json
    scan_dto = ScanJSON(**body)

    qr_code_id = scan_dto.qr_code_id
    date = get_time_from_iso(scan_dto.date)

    scan_qr_code(qr_code_id, date)

    return {}
  
  except ValidationError:
    raise BadRequestException
