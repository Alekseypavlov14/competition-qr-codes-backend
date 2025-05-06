from flask import Flask, json, request, jsonify
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
from db import db
import config
import api

# create app
app = Flask(__name__)

# setup cors
CORS(app, origins="*", allow_headers=["Authorization", "Content-Type"], methods=["GET", "POST", "OPTIONS"])

# handle preflight requests
@app.before_request
def handle_options():
  if request.method == "OPTIONS":
    response = jsonify()
    
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    
    return response
  
# handle headers after request
@app.after_request
def handle_headers(response):
  response.headers["Access-Control-Expose-Headers"] = "Authorization"
  return response

# add db data
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init app
db.init_app(app)
app.register_blueprint(api.router) 

@app.errorhandler(HTTPException)
def handle_exception(e):
  response = e.get_response()

  response.data = json.dumps({ "code": e.code })
  response.content_type = "application/json"

  return response

if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run(host=config.host, port=config.port)
