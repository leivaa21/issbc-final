from src.model.Tests import (AnthropometricMeasurementTest, CardioRespiratoryTest, 
                              BlodAndUrineTest, EffortTest)

def isEqual(meassure, expected) -> bool:
  return (meassure == expected)

def isInRange(meassure: float, start: float, end: float) -> bool:
  return (meassure > start and meassure < end)

def rule1(cardioRespiratoryTest:CardioRespiratoryTest, bloodAndUrineTest: BlodAndUrineTest) -> bool:
  if isEqual(cardioRespiratoryTest.hasPassed, False) and isEqual(bloodAndUrineTest.doping, True):
    return True
  return False

def rule2(anthropometricMeasurementTest: AnthropometricMeasurementTest):
  return isInRange(anthropometricMeasurementTest.bmi, 18.5, 27)

def rule3(effortTest: EffortTest) -> bool:
  return isInRange(effortTest.oxigenAerobic, 50, 70) and isInRange(effortTest.oxigenAnaerobic, 50, 70)
