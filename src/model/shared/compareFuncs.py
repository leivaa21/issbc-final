def isEqual(meassure, expected) -> bool:
  return meassure == expected

def isInRange(meassure: float, start: float, end: float) -> bool:
  return (meassure >= start and meassure <= end)
