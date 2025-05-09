from flask import Blueprint, request, Response
from pydantic import ValidationError
from api.exceptions import BadRequestException, UnauthorizedException
from services.auth.headers import get_auth_header
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

@router.get('/verification')
def verify_token():
  token = get_auth_header()
  if not token: raise UnauthorizedException

  actions.verify_token(token)

  return Response("{}", headers={ 'Authorization': token })