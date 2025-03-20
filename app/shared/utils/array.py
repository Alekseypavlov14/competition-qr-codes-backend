def for_each(lst, callback):
  for item in lst:
    callback(item)

def map(lst, callback):
  return [callback(item) for item in lst]

def filter(lst, callback):
  return [item for item in lst if callback(item)]