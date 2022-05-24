from controller.domain import DomainController
from controller.evalue import EvaluatorController
from controller.storage import StorageController


params = {
  "name":"SuperSano",
  "age": 18,
  "oxigenAerobic": 50,
  "oxigenAnaerobic": 70,
  "passedCardio": True,
  "doping": False,
  "suspiciousSubstances": True,
  "weightInKg": 80,
  "heightInCm": 188,
  "mmi": 20.4
}

params2 = {
  "name":"AntiSano",
  "age": 19,
  "oxigenAerobic": 40,
  "oxigenAnaerobic": 80,
  "passedCardio": True,
  "doping": True,
  "suspiciousSubstances": True,
  "weightInKg": 800,
  "heightInCm": 188,
  "mmi": 20.4
}

Domain = DomainController('footballPlayer')
Storage = StorageController()

case1 = Domain.generateCase(params);
case2 = Domain.generateCase(params2);

Storage.saveOne(case1)
Storage.saveOne(case2)

Evalue = EvaluatorController(Domain, Storage)
response = Evalue.evalueAll([True, False, True])
for inform in response.items():
  print('-----')
  print('Identifier: ' + inform[0])
  print('Results: ' + str(inform[1]))
  print('-----')
