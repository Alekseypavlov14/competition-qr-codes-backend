from flask import Blueprint
import api.v1.auth as auth
import api.v1.qr_code as qr_code
import api.v1.analytics as analytics

router = Blueprint('v1', __name__, url_prefix='/v1')

router.register_blueprint(auth.router)
router.register_blueprint(qr_code.router)
router.register_blueprint(analytics.router)
