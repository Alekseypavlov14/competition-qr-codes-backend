from flask import request
from shared.const import auth_header

def get_auth_header(): 
  return request.headers.get(auth_header)
