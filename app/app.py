from werkzeug.exceptions import HTTPException
from flask import Flask, json
from db import db
import config
import api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
