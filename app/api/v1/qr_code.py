# libs
from pydantic import ValidationError
from flask import Blueprint, request

# models
from models.qr_code import QRCode

# services
from services.auth.middlewares import auth_required
from services.auth.headers import get_auth_header
from services.qr_code.dto import QRCodeDTO
from services.qr_code.actions import create_qr_code
from services.serialization.qr_code import get_qr_code_dict
from services.users.actions import get_qr_codes_by_token

# shared
from api.exceptions import BadRequestException, UnauthorizedException, NotFoundException

router = Blueprint('qr_codes', __name__, url_prefix='/qr-codes')

@auth_required
@router.get('/')
def get():
  try:
    token = get_auth_header()
    if not token: raise UnauthorizedException

    qr_codes = get_qr_codes_by_token(token)
    qr_codes_dicts = map(get_qr_code_dict, qr_codes)

    return list(qr_codes_dicts)
  
  except:
    raise BadRequestException

@auth_required
@router.post('/')
def create():
  try:
    body = request.json
    qr_code_dto = QRCodeDTO(**body)

    qr_code = create_qr_code(qr_code_dto)
    qr_code_dict = get_qr_code_dict(qr_code)

    return qr_code_dict

  except ValidationError:
    raise BadRequestException
  
@auth_required
@router.get('/<int:id>')
def get_by_id(id):
  try:
    qr_code = QRCode.query.filter_by(id=id).first()
    if not qr_code: raise NotFoundException

    return get_qr_code_dict(qr_code)
  except:
    BadRequestException
  