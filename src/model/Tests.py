class MedicTest:
  def __init__(self, testType, footballPlayerName, footballPlayerAge):
    self.type = testType
    self.footballPlayerName = footballPlayerName
    self.footballPlayerAge = footballPlayerAge

# Specific tests

class EffortTest(MedicTest):
  def __init__(self, fpName, fpAge, oxigenAerobic, oxigenAnaerobic, hasCardioProblems):
    super().__init__('EffortTest', fpName, fpAge)
    self.oxigenAerobic = oxigenAerobic
    self.oxigenAnaerobic = oxigenAnaerobic
    self.hasCardioProblems = hasCardioProblems

class CardioRespiratoryTest(MedicTest):
  def __init__(self, fpName, fpAge, hasPassed):
    super().__init__('EffortTest', fpName, fpAge)
    self.hasPassed = hasPassed

class BlodAndUrineTest(MedicTest):
  def __init__(self, fpName, fpAge, doping, suspiciousSubstances):
    super().__init__('EffortTest', fpName, fpAge)
    self.doping = doping
    self.suspiciousSubstances = suspiciousSubstances

class AnthropometricMeasurementTest(MedicTest):
  def __init__(self, fpName, fpAge, weightInKg, heightInCm, mmi):
    super().__init__('EffortTest', fpName, fpAge)
    self.height = heightInCm
    self.weight = weightInKg
    self.mmi = mmi
    self.bmi = weightInKg / pow(heightInCm / 100, 2)