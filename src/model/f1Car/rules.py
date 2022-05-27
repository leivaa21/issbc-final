from model.shared.compareFuncs import greaterEqualsThan, isEqual, isInRange, lessEqualsThan
from model.f1Car.f1Car import f1Car


def rule1(car: f1Car) -> bool:
    totalWeight = car.weight + car.weight_test.pilotWeight
    test1 = greaterEqualsThan(totalWeight, 740)
    return test1


def rule2(car: f1Car) -> bool:
    tire_test = car.tire_test
    test1 = lessEqualsThan(tire_test.backTireWidth, 405)
    test2 = lessEqualsThan(tire_test.frontTireWidth, 305)
    return test1 and test2


def rule3(car: f1Car) -> bool:
    spoiler_test = car.back_spoiler_test
    test1 = isInRange(spoiler_test.width_in_mm, 84, 95)
    test2 = isInRange(spoiler_test.height_in_mm, 75, 80)
    return test1 and test2
