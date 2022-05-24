import importlib
from typing import Dict


class DomainController:
  # Domains contempled on the application
  __domains = ['footballPlayer', 'f1Car']
  def __init__(self, domain) -> None:
    if self.__domains.__contains__(domain):
      self._domain = domain;
    self._domain = self.__domains[0]

  def generateCase(self, params: Dict):
    model = self.__get_model()
    case = model(params)
    return case

  def __get_model(self):
    module_name = "model." + self._domain + "." + self._domain
    module = importlib.import_module(module_name)
    class_name = self._domain
    return getattr(module, class_name)
