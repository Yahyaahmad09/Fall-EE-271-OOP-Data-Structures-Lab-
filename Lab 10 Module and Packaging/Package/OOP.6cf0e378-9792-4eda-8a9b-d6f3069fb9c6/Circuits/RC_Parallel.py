# RC parallel

import cmath
import math

class RC_parallel_circuit:
    def __init__(self, R, X_C, E):
        """
        Initialize the RC parallel circuit with resistance, capacitive reactance, and source voltage.
        :param R: Resistance in ohms
        :param X_C: Capacitive reactance in ohms
        :param E: Voltage source in polar form (magnitude, angle in degrees)
        """
        self.R = R
        self.X_C = X_C
        self.E = self.Complex(E)

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
        self._X_C = value

    @property
    def E(self):
        return self.Polar(self._E)

    @E.setter
    def E(self, value: tuple):
        self._E = self.Complex(value)

    @staticmethod
    def Polar(value: complex):
        """
        Convert a complex number to polar form.
        :param value: Complex number
        :return: Tuple (magnitude, angle in degrees)
        """
        magnitude = abs(value)
        angle = cmath.phase(value)
        angle_deg = angle * (180 / cmath.pi)
        return magnitude, angle_deg

    @staticmethod
    def Complex(polar: tuple) -> complex:
        """
        Convert polar form to a complex number.
        :param polar: Tuple (magnitude, angle in degrees)
        :return: Complex number
        """
        magnitude, angle_deg = polar
        angle_rad = angle_deg * (cmath.pi / 180)
        return cmath.rect(magnitude, angle_rad)

    @property
    def Y(self):
        """
        Calculate the admittance (Y) of the parallel RC circuit.
        :return: Admittance in polar form
        """
        G = 1 / self.R  # Conductance
        B_C = 1 / self.X_C  # Susceptance (for the capacitor)
        admittance = G + 1j * B_C
        return self.Polar(admittance)

    @property
    def Z(self):
        """
        Calculate the impedance (Z) of the parallel RC circuit.
        :return: Impedance in polar form
        """
        admittance = self.Y  # Admittance
        impedance = 1 / (self.Complex(admittance))
        return self.Polar(impedance)

    @property
    def I(self):
        """
        Calculate the total current in the circuit based on the voltage and admittance.
        :return: Current in polar form
        """
        admittance = self.Y  # Admittance
        current = self._E * admittance
        return self.Polar(current)

    @property
    def I_R(self):
        """
        Calculate the current through the resistor.
        :return: Current in polar form
        """
        current_r = self._E / self.R
        return self.Polar(current_r)

    @property
    def I_C(self):
        """
        Calculate the current through the capacitor.
        :return: Current in polar form
        """
        current_c = self._E / self.X_C
        return self.Polar(current_c)

    @property
    def P(self):
        """
        Calculate the power dissipated in the resistor.
        :return: Power in watts
        """
        return abs(self._E) ** 2 / self.R

    @property
    def P_f(self) -> float:
        """
        Calculate the power factor of the circuit.
        :return: Power factor as a float
        """
        admittance = self.Y  # Admittance
        impedance = 1 / admittance
        return abs(impedance.real) / abs(impedance)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(R={self.R}, X_C={self.X_C}, E={self.E})"

    def __str__(self) -> str:
        return f"RC Parallel Circuit with R={self.R} ohm, X_C={self.X_C} ohm, E={self.E} V"
