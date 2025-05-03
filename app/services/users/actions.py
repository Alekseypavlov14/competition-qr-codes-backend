from models.user import User
from models.qr_code import QRCode
from models.session import Session

def get_qr_codes_by_token(token: str):
  session: Session = Session.query.filter_by(token=token).first()
  if not session: return []

  user: User = User.query.filter_by(id=session.user_id).first()
  if not user: return []

  qr_codes: list[QRCode] = QRCode.query.filter_by(user_id=user.id).all()

  return qr_codes
