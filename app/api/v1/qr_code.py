from services.auth.middlewares import auth_required
from services.qr_code.qr_code import get_qr_code_dict
from services.qr_code.actions import create_qr_code
from services.qr_code.dto import QRCodeDTO
from api.exceptions import BadRequestException
from pydantic import ValidationError
from flask import Blueprint, request

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