import numpy as np
from sympy import false

from .base_model import BasePopulationModel


class MalthusModel(BasePopulationModel):
    def get_parameters(self):
        return [('P0', 100), ('r', 0.1), ('time', 50)]

    def validate_parameters(self, params):
        required = ['P0', 'r', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):
        p = params['P0'] * np.exp(params['r'] * time_values)
        return p

    def get_name(self):
        return "Modelo de Malthus"

    def is_discrete(self):
        return False

class DiscreteModel(BasePopulationModel):
    def get_parameters(self):
        return [('P0', 100), ('r', 0.1), ('K', 500), ('time', 50)]

    def validate_parameters(self, params):
        required = ['P0', 'r', 'K', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):
        p = np.zeros_like(time_values)
        p[0] = params['P0']
        for t in range(1, len(time_values)):
            p[t] = p[t - 1] + params['r'] * p[t - 1] * (1 - p[t - 1] / params['K'])
        return p

    def get_name(self):
        return "Modelo de Verhulst Simplificado"

    def is_discrete(self):
        return True


class LogisticModel(BasePopulationModel):
    def get_parameters(self):
        return [('P0', 100), ('r', 0.1), ('K', 500), ('time', 50)]

    def validate_parameters(self, params):
        required = ['P0', 'r', 'K', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):
        dt = time_values[1] - time_values[0]
        p = np.zeros_like(time_values)
        p[0] = params['P0']
        for t in range(1, len(time_values)):
            dp = params['r'] * p[t - 1] * (1 - p[t - 1] / params['K']) * dt
            p[t] = p[t - 1] + dp
        return p

    def get_name(self):
        return "Modelo Logístico de Verhulst"

    def is_discrete(self):
        return false


class DelayedLogisticModel(BasePopulationModel):
    def get_parameters(self):
        return [('P0', 100), ('r', 0.1), ('K', 500), ('tau', 1), ('time', 50)]

    def validate_parameters(self, params):
        required = ['P0', 'r', 'K', 'tau', 'time']
        return all(key in params for key in required)

    def calculate(self, params, time_values):
        dt = time_values[1] - time_values[0]
        tau_steps = int(params['tau'] / dt)
        p = np.zeros_like(time_values)
        p[:tau_steps + 1] = params['P0']

        for t in range(tau_steps + 1, len(time_values)):
            dp = params['r'] * p[t - 1] * (1 - p[t - tau_steps - 1] / params['K']) * dt
            p[t] = p[t - 1] + dp
        return p

    def get_name(self):
        return "Modelo Logístico de Verhulst con Retardo"
    def is_discrete(self):
        return false