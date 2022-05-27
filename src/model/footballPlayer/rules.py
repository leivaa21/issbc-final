from model.shared.compareFuncs import isEqual, isInRange
from model.footballPlayer.footballPlayer import footballPlayer


def rule1(player: footballPlayer) -> bool:
    cardioRespiratoryTest = player.cardioRespiratoryTest
    bloodAndUrineTest = player.bloodAndUrineTest

    test1 = isEqual(cardioRespiratoryTest.hasPassed, True)
    test2 = isEqual(bloodAndUrineTest.doping, False)

    return test1 and test2


def rule2(player: footballPlayer):
    anthropometricMeasurementTest = player.anthropometricMeasurementTest
    test1 = isInRange(anthropometricMeasurementTest.bmi, 18.5, 27)
    return test1


def rule3(player: footballPlayer) -> bool:
    effortTest = player.effortTest
    test1 = isInRange(effortTest.oxigenAerobic, 50, 70)
    test2 = isInRange(effortTest.oxigenAnaerobic, 50, 70)
    return test1 and test2
