import importlib
from model.shared.domainList import domainList
from typing import Dict


class DomainController:
    # Domains contempled on the application

    def __init__(self, domain) -> None:

        if domainList.__contains__(domain):
            self._domain = domain
        else:
            self._domain = domainList[0]

    def generateCase(self, params: Dict):
        model = self.__get_model()
        case = model(params)
        return case

    def __get_model(self):
        module_name = "model." + self._domain + "." + self._domain
        module = importlib.import_module(module_name)
        class_name = self._domain
        return getattr(module, class_name)
