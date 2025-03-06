from flask import Blueprint, request
from api.exceptions import BadRequestException
from services.auth import actions, Credentials

router = Blueprint('auth', __name__, url_prefix='/auth')

@router.get('/sign-in')
def sign_in():
  try: 
    body = request.json
    credentials = Credentials(**body)

    token = actions.sign_in(credentials)

    return { 'Message': 'Sign in', 'token': token }
  except:
    raise BadRequestException

@router.get('/sign-up')
def sign_up():
  credentials = Credentials()
  credentials.email = 'aleshapavlov9@gmail.com'
  credentials.password = '12345678'

  token = actions.sign_up(credentials)

  return { 'Message': 'Sign up', 'token': token }