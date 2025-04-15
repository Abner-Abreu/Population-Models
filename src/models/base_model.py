from abc import ABC, abstractmethod

class BasePopulationModel(ABC):

    @abstractmethod
    def get_parameters(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def validate_parameters(self,params):
        pass

    @abstractmethod
    def calculate(self, params, time):
        pass

    @abstractmethod
    def is_discrete(self):
        pass