from flask import Blueprint
import api.v1 as v1

router = Blueprint('api', __name__, url_prefix='/api')

router.register_blueprint(v1.router)
