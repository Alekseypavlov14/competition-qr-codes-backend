from flask import Blueprint, request, Response
from pydantic import ValidationError
from api.exceptions import BadRequestException
from services.auth import actions, Credentials

router = Blueprint('auth', __name__, url_prefix='/auth')

@router.post('/sign-in')
def sign_in():
  try: 
    body = request.json
    credentials = Credentials(**body)

    token = actions.sign_in(credentials)

    return Response("{}", headers={ 'Authorization': token })
  except ValidationError:
    raise BadRequestException

@router.post('/sign-up')
def sign_up():
  try:
    body = request.json
    credentials = Credentials(**body)

    token = actions.sign_up(credentials)

    return Response("{}", headers={ 'Authorization': token })
  except ValidationError:
    raise BadRequestException
