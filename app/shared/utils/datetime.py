from datetime import datetime

def get_time_from_iso(iso_date: str) -> datetime:
  return datetime.fromisoformat(iso_date)
