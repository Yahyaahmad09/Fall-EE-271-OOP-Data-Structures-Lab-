# RL parallel
import cmath
import math
class RL_parallel_circuit:
    def __init__(self, R, X_L, V):
        self.R = R
        self.X_L = X_L
        self.V = V

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, value: float):
        self._R = value

    @property
    def X_L(self):
        return self._X_L

    @X_L.setter
    def X_L(self, value: float):
        self._X_L = value * 1j

    @property
    def V(self):
        return self.Polar(self._V)

    @V.setter
    def V(self, value: tuple):
        self._V = self.Complex(value)

    @staticmethod
    def Polar(value: complex):
        magnitude = abs(value)
        angle = cmath.phase(value)
        angle_deg = angle * (180 / cmath.pi)
        return magnitude, angle_deg

    @staticmethod
    def Complex(polar: tuple) -> complex:
        magnitude, angle_deg = polar
        angle_rad = angle_deg * (cmath.pi / 180)
        return cmath.rect(magnitude, angle_rad)

    @property
    def G(self):
        return 1 / self._R

    @property
    def B_L(self):
        return -1 / self._X_L

    @property
    def Y(self):
        y = self.G + self.B_L
        return self.Polar(y)

    @property
    def Z(self):
        z = 1 / self.Complex(self.Y)
        return self.Polar(z)

    @property
    def I(self):
        i = self._V / self.Complex(self.Z)
        return self.Polar(i)

    @property
    def I_R(self):
        i_r = self._V / self._R
        return self.Polar(i_r)

    @property
    def I_L(self):
        i_l = self._V / self._X_L
        return self.Polar(i_l)

    @property
    def P(self):
        return abs(self._V)**2 * self.G

    @property
    def P_f(self) -> float:
        y = self.G + self.B_L
        return self.G / abs(y)

    def __repr__(self) -> str:
        return f"{type(self).__name__} ({self.R},{self.X_L})"

    def __str__(self) -> str:
        return f"RL Parallel Circuit with resistance: {self.R} ohm, inductive reactance: {self.X_L} H"
