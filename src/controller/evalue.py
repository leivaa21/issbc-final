from array import array
import importlib
from types import NoneType
from controller.storage import StorageController
from controller.domain import DomainController


class EvaluatorController:
    def __init__(self, domain: DomainController, storage: StorageController):
        self.domainController = domain
        self.storageController = storage

    def evalueAll(self, applyArray: array):
        res = {}
        for case in self.storageController.getCases():
            res[case.identificator()] = {}
            for index in range(3):
                if applyArray[index]:
                    rulename = 'rule' + str(index + 1)
                    res[case.identificator()][rulename] = self.__evalueRuleInCase(
                        case, index + 1)
        return res

    def evalueOne(self, identificator, applyArray: array):
        case = self.storageController.getOne(identificator)
        if type(case) == NoneType:
            return
        res = {}
        res[case.identificator()] = {}
        for index in range(3):
            if applyArray[index]:
                rulename = 'rule' + str(index + 1)
                res[case.identificator()][rulename] = self.__evalueRuleInCase(
                    case, index + 1)
        return res

    def __evalueRuleInCase(self, case, ruleIndex) -> bool:
        rule = self.__getRule(ruleIndex)
        return rule(case)

    def __getRule(self, number: int):
        if int(number) > 3 or int(number) < 1:
            number = 1
        rule = self.___get_rule(number)
        return rule

    def ___get_rule(self, number: int):
        module_name = "model." + self.domainController._domain + ".rules"
        module = importlib.import_module(module_name)
        rule_name = 'rule' + str(number)
        return getattr(module, rule_name)
