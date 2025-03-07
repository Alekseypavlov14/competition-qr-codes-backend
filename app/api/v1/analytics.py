from flask import Blueprint, request
from pydantic import ValidationError
from api.exceptions import BadRequestException
from services.auth.middlewares import auth_required
from services.analytics import ScanJSON, scan_qr_code
from shared.utils.datetime import get_time_from_iso

router = Blueprint('analytics', __name__, url_prefix='/analytics')

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
