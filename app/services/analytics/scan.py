from models.scan import Scan

def get_scan_dict(scan: Scan):
  return ({
    'id': scan.id,
    'date': scan.date.isoformat(timespec='seconds'),
    'qr_code_id': scan.qr_code_id
  })
