# libs
from pydantic import ValidationError
from flask import Blueprint, request

# services
from services.auth.middlewares import auth_required
from services.qr_code.scan import ScanJSON
from services.qr_code.actions import scan_qr_code
from services.auth.middlewares import auth_required

# shared
from shared.utils.datetime import get_time_from_iso
from api.exceptions import BadRequestException

router = Blueprint('analytics', __name__, url_prefix='/analytics')

@auth_required
@router.post('/scan')
def scan():
  try: 
    body = request.json
    scan_dto = ScanJSON(**body)

    hash = scan_dto.hash
    date = get_time_from_iso(scan_dto.date)

    scan_qr_code(hash, date)

    return {}
  
  except ValidationError:
    raise BadRequestException
