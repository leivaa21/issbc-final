from model.shared.compareFuncs import isEqual, isInRange
from model.footballPlayer.footballPlayer import footballPlayer

def rule1(player: footballPlayer) -> bool:
  cardioRespiratoryTest = player.cardioRespiratoryTest
  bloodAndUrineTest = player.bloodAndUrineTest
  
  axiom1 = isEqual(cardioRespiratoryTest.hasPassed, True)
  axiom2 = isEqual(bloodAndUrineTest.doping, False)

  return axiom1 and axiom2 

def rule2(player: footballPlayer):
  anthropometricMeasurementTest = player.anthropometricMeasurementTest
  axiom1 = isInRange(anthropometricMeasurementTest.bmi, 18.5, 27)
  return axiom1

def rule3(player: footballPlayer) -> bool:
  effortTest = player.effortTest
  axiom1 = isInRange(effortTest.oxigenAerobic, 50, 70)
  axiom2 = isInRange(effortTest.oxigenAnaerobic, 50, 70)
  return axiom1 and axiom2
