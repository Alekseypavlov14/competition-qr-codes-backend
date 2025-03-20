# libs
from pydantic import ValidationError
from flask import Blueprint, request

# services
from services.auth.middlewares import auth_required
from services.analytics.actions import get_qr_code_analytics 
from services.analytics.qr_code import QRCodeDTO

# shared
from api.exceptions import BadRequestException

router = Blueprint('analytics', __name__, url_prefix='/analytics')

@auth_required
@router.get('/qr-code')
def get_analytics():
  try:
    body = request.json
    qr_code_dto = QRCodeDTO(**body)

    qr_code_analytics = get_qr_code_analytics(qr_code_dto.id)

    return qr_code_analytics

  except ValidationError:
    raise BadRequestException
