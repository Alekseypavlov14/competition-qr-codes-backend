from datetime import datetime

def get_time_from_iso(iso_date: str) -> datetime:
  return datetime.strptime(iso_date, '%Y-%m-%dT%H:%M:%S.%fZ')
