
import string


class f1Car:

    def __init__(self, params):
        self.brand = params['brand']
        self.model = params['model']
        self.weight = float(params['weight_in_kg'])

        self.weight_test = WeightTest(
            self, float(params['pilot_weight_in_kg']))
        self.tire_test = TireTest(
            self, int(params['front_tire_width_in_mm']), int(params['back_tire_width_in_mm']))
        self.back_spoiler_test = BackSpoilerTest(
            self, int(params['spoiler_width_in_mm']), int(params['spoiler_height_in_mm']))

    def identificator(self):
        return self.brand + ' ' + self.model


class MechanicTest:
    def __init__(self, testType: string, car: f1Car):
        self.testType = testType
        self.carTeam = car.brand
        self.carModel = car.model


class WeightTest(MechanicTest):
    def __init__(self, car: f1Car, pilotWeight: float):
        super().__init__('Weight Test', car)
        self.pilotWeight = pilotWeight


class TireTest(MechanicTest):
    def __init__(self, car: f1Car, frontTireWidth_in_mm: int, backTireWidth_in_mm: int):
        super().__init__('Tire Test', car)
        self.frontTireWidth = frontTireWidth_in_mm
        self.backTireWidth = backTireWidth_in_mm


class BackSpoilerTest(MechanicTest):
    def __init__(self, car: f1Car, width_in_mm: int, height_in_mm: int):
        super().__init__('Back Spoiler Test', car)
        self.width_in_mm = width_in_mm
        self.height_in_mm = height_in_mm
