from flask import Blueprint
import api.v1.auth as auth

router = Blueprint('v1', __name__, url_prefix='/v1')

router.register_blueprint(auth.router)
