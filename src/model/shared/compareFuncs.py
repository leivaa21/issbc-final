def isEqual(meassure, expected) -> bool:
    return meassure == expected


def isInRange(meassure: float, start: float, end: float) -> bool:
    return (meassure >= start and meassure <= end)


def greaterEqualsThan(meassure, value) -> bool:
    return meassure >= value


def lessEqualsThan(meassure, value) -> bool:
    return meassure <= value
