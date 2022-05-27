import string
from model.shared.helpers import str_to_bool


class footballPlayer:

    def __init__(self, params):
        self.name = params['name']
        self.age = int(params['age'])
        self.effortTest = EffortTest(
            self,
            float(params['oxigenAerobic']),
            float(params['oxigenAnaerobic']),
            str_to_bool(params['passedCardio']) != True
        )

        self.cardioRespiratoryTest = CardioRespiratoryTest(
            self,
            str_to_bool(params['passedCardio'])
        )
        self.bloodAndUrineTest = BloodAndUrineTest(
            self,
            str_to_bool(params['doping']),
            str_to_bool(params['suspiciousSubstances'])
        )
        self.anthropometricMeasurementTest = AnthropometricMeasurementTest(
            self,
            float(params['weightInKg']),
            int(params['heightInCm']),
            float(params['mmi'])
        )

    def identificator(self):
        return self.name


# General Test


class MedicTest:
    def __init__(self, testType: string, player: footballPlayer):
        self.type = testType
        self.footballPlayerName = player.name
        self.footballPlayerAge = player.age

# Specific tests


class EffortTest(MedicTest):
    def __init__(self, player: footballPlayer, oxigenAerobic: float, oxigenAnaerobic: float, hasCardioProblems: bool):
        super().__init__('Effort Test', player)
        self.oxigenAerobic = oxigenAerobic
        self.oxigenAnaerobic = oxigenAnaerobic
        self.hasCardioProblems = hasCardioProblems


class CardioRespiratoryTest(MedicTest):
    def __init__(self, player: footballPlayer, hasPassed: bool):
        super().__init__('Cardio Respiratory', player)
        self.hasPassed = hasPassed


class BloodAndUrineTest(MedicTest):
    def __init__(self, player: footballPlayer, doping: bool, suspiciousSubstances: bool):
        super().__init__('Blood And Urine', player)
        self.doping = doping
        self.suspiciousSubstances = suspiciousSubstances


class AnthropometricMeasurementTest(MedicTest):
    def __init__(self, player: footballPlayer, weightInKg: float, heightInCm: int, mmi: float):
        super().__init__('Anthropometric Measurement', player)
        self.height = heightInCm
        self.weight = weightInKg
        self.mmi = mmi
        self.bmi = int(weightInKg) / pow(int(heightInCm) / 100, 2)
