# RlC Parallel circuit

import cmath

class RLC_parallel_circuit:
    def __init__(self, R, X_L, X_C, I):
        self._R = R
        self._X_L = X_L
        self._X_C = X_C
        self._I = self.Complex(I)

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, value):
        self._R = value

    @property
    def X_L(self):
        return self._X_L

    @X_L.setter
    def X_L(self, value):
        self._X_L = value

    @property
    def X_C(self):
        return self._X_C

    @X_C.setter
    def X_C(self, value):
        self._X_C = value

    @property
    def I(self):
        return self.Polar(self._I)

    @I.setter
    def I(self, value):
        self._I = self.Complex(value)

    @property
    def admittance_resistor(self):
        Y_R = 1 / self._R
        return Y_R

    @property
    def admittance_inductor(self):
        Y_L = 1 / (self._X_L * 1j)
        return Y_L

    @property
    def admittance_capacitor(self):
        Y_C = 1 / (self._X_C * -1j)
        return Y_C

    @property
    def impedance(self):
        Y_total = self.admittance_resistor + self.admittance_inductor + self.admittance_capacitor
        Z_total = 1 / Y_total if Y_total != 0 else float('inf')
        return self.Polar(Z_total)

    @property
    def voltage(self):
        Z = self.Complex(self.impedance)
        V = self._I * Z
        return self.Polar(V)

    @property
    def power(self):
        V = abs(self.Complex(self.voltage))
        P = V**2 / self.R
        return P

    @property
    def power_factor(self):
        Z = self.Complex(self.impedance)
        return cmath.cos(cmath.phase(Z))

    @staticmethod
    def Polar(value: complex) -> tuple:
        magnitude = abs(value)
        angle = cmath.phase(value)
        angle_degrees = angle * (180 / cmath.pi)
        return magnitude, angle_degrees

    @staticmethod
    def Complex(polar: tuple) -> complex:
        magnitude, angle_degrees = polar
        angle_radians = angle_degrees * (cmath.pi / 180)
        return cmath.rect(magnitude, angle_radians)

    def __repr__(self):
        return f'{type(self).__name__} (R={self.R}, L={self.X_L}, C={self.X_C})'

    def __str__(self):
        return f'RLC Parallel Circuit with Resistance = {self.R}, Inductance = {self.X_L}, Capacitance = {self.X_C}'
