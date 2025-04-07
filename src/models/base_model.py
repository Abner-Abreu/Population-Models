from abc import ABC, abstractmethod

class BasePopulationModel(ABC):

    name = None
    discrete = False

    @abstractmethod
    def get_parameters(self):
        pass

    @abstractmethod
    def validate_parameters(self,params):
        pass

    @abstractmethod
    def calculate(self, params, time):
        pass