from werkzeug.exceptions import HTTPException
from flask import Flask, json
from flask_cors import CORS
from db import db
import config
import api

# create app
app = Flask(__name__)

# add db data
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# setup cors
CORS(app, origins="*", allow_headers=["Authorization", "Content-Type"], methods=["GET", "POST", "OPTIONS"])

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
