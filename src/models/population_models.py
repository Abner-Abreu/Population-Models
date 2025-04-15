import numpy as np
from ddeint import ddeint
from .base_model import BasePopulationModel


class MalthusModel(BasePopulationModel):

    def get_parameters(self):
        return [('P0', 100), ('r', 0.1), ('time', 50)]

    def get_name(self):
        return "Modelo de Malthus"

    def validate_parameters(self, params):
        required = ['P0', 'r', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):
        p = params['P0'] * np.exp(params['r'] * time_values)
        return p

    def is_discrete(self):
        return False

class DiscreteModel(BasePopulationModel):

    def get_parameters(self):
        return [('P0', 0.3), ('r', 3.75), ('time', 50)]

    def get_name(self):
        return "Modelo Logístico de Verhulst (Discreto)"

    def validate_parameters(self, params):
        required = ['P0', 'r', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):
        p = np.zeros_like(time_values)
        p[0] = params['P0']
        for t in range(1, len(time_values)):
            p[t] = p[t-1] * params['r'] * (1 - p[t-1])
        return p

    def is_discrete(self):
        return True


class LogisticModel(BasePopulationModel):

    def get_parameters(self):
        return [('P0', 100), ('r', 0.1), ('K', 500), ('time', 50)]

    def get_name(self):
        return "Modelo Logístico de Verhulst (Contínua)"

    def validate_parameters(self, params):
        required = ['P0', 'r', 'K', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):
        p = params['K'] / (1 + (params['K'] / params['P0'] - 1) * np.exp(-1 * params['r'] * time_values))
        return p

    def is_discrete(self):
        return False

class DelayedLogisticModel(BasePopulationModel):

    def get_parameters(self):
        return [('P0', 100), ('r', 0.4), ('K', 500), ('tau', 3), ('time', 50)]

    def get_name(self):
        return "Modelo de Hutchinson"

    def validate_parameters(self, params):
        required = ['P0', 'r', 'K', 'tau', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):

        def equation(p, t):
            return params['r'] * p(t) * (1 - p(t - params['tau']) / params['K'])

        def history(t):
            return params['P0']

        solution = ddeint(equation, history, time_values)
        return solution.flatten()

    def is_discrete(self):
        return False
