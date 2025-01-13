# RC series

import cmath
import math
class RC_series_circuit:
    def __init__(self, R, X_C, I):
        self.R = R
        self.X_C = X_C
        self.I = I
    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, value: float):
        self._R = value

    @property
    def X_C(self):
        return self._X_C

    @X_C.setter
    def X_C(self, value: float):
        self._X_C = value * -1j

    @property
    def I(self):
        return self.Polar(self._I)

    @I.setter
    def I(self, value: tuple):
        self._I = self.Complex(value)
    
    @staticmethod
    def Polar( value: complex):
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
    def Z(self):
        z = self.R + self._X_C
        return self.Polar(z)
    @property
    def V(self):
        v =  (self._I) * (self.Complex(self.Z))
        return self.Polar(v)
    @property
    def V_R(self):
        v_r = (self._I) * (self._R)
        return self.Polar(v_r)
    @property
    def V_C(self):
        v_c = (self._I) * (self._X_C)
        return self.Polar((v_c))
                                     
    @property
    def P(self):
        return abs(self._I)**2 * self._R
    @property
    def P_f(self) -> float:
        z = self._R + self._X_C
        return self._R / abs(z)

    def __repr__(self) -> str:
        return f"{type(self).__name__} ({self.R},{self.X_C})"

    def __str__(self) -> str:
        return f"RC Series Circuit with resistance: {self.R} ohm, capacitance: {self.C} F"
