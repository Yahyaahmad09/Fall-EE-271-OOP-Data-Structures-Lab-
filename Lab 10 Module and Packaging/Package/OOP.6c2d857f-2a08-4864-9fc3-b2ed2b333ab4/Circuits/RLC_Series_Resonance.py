# RLC Series Resonance Circuit

import math

class RLC_series_resonance_circuit:
    def __init__(self, R, L, C):
        self.R = R
        self.L = L
        self.C = C

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, value):
        self._R = value

    @property
    def L(self):
        return self._L

    @L.setter
    def L(self, value):
        self._L = value

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        self._C = value

    def Resonance_f(self):
        return 1 / (2 * math.pi * math.sqrt(self._L * self._C))

    def Q_factor(self):
        return 1 / (self._R * math.sqrt(self._C / self._L))

    def Band_width(self):
        return self.Resonance_f() / self.Q_factor()

    def f1(self):
        return self.Resonance_f() - (self.Band_width() / 2)

    def f2(self):
        return self.Resonance_f() + (self.Band_width() / 2)

    @staticmethod
    def Voltage(V, Z):
        return V / Z  

    def __repr__(self):
        return f'{type(self).__name__} ({self.R}, {self.L}, {self.C})'

    def __str__(self):
        return f'RLC Resonance Series Circuit with Resistance: {self.R}, Inductance: {self.L}, Capacitance: {self.C}'
