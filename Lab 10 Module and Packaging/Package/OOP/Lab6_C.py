# RL series
import cmath
import math

class RL_series_circuit:
    def __init__(self, R, X_L, I):
        self.R = R
        self.X_L = X_L
        self.I = I

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
    def I(self):
        return self.Polar(self._I)

    @I.setter
    def I(self, value: tuple):
        self._I = self.Complex(value)

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
    def Z(self):
        z = self.R + self._X_L
        return self.Polar(z)

    @property
    def V(self):
        v = self._I * self.Complex(self.Z)
        return self.Polar(v)

    @property
    def V_R(self):
        v_r = self._I * self._R
        return self.Polar(v_r)

    @property
    def V_L(self):
        v_l = self._I * self._X_L
        return self.Polar(v_l)

    @property
    def P(self):
        return abs(self._I)**2 * self._R

    @property
    def P_f(self) -> float:
        z = self._R + self._X_L
        return self._R / abs(z)

    def __repr__(self) -> str:
        return f"{type(self).__name__} ({self.R},{self.X_L})"

    def __str__(self) -> str:
        return f"RL Series Circuit with resistance: {self.R} ohm, inductive reactance: {self.X_L} H"


# ------------------------------------------------------------------------------------------------------------------------------

# RL parallel

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


# ------------------------------------------------------------------------------------------------------------------------------

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


# ------------------------------------------------------------------------------------------------------------------------------

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


# ------------------------------------------------------------------------------------------------------------------------------


import cmath

class RLC_series_circuit:
    def __init__(self, R, X_L, X_C, V):
        self._R = R  
        self._X_L = X_L * 1j 
        self._X_C = X_C * -1j  
        self._V = self.Complex(V)  

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
        self._X_L = value * 1j

    @property
    def X_C(self):
        return self._X_C

    @X_C.setter
    def X_C(self, value):
        self._X_C = value * -1j

    @property
    def V(self):
        return self.Polar(self._V)

    @V.setter
    def V(self, value):
        self._V = self.Complex(value)

    @property
    def impedance(self):
        Z_total = self._R + self._X_L + self._X_C
        return self.Polar(Z_total)

    @property
    def current(self):
        Z = self.Complex(self.impedance)
        I = self._V / Z
        return self.Polar(I)

    @property
    def power(self):
        # Calculate power: P = |I|^2 * R
        I_magnitude = abs(self.Complex(self.current))
        P = (I_magnitude**2) * self.R
        return P

    @property
    def power_factor(self):
        Z = self.Complex(self.impedance)
        return cmath.cos(cmath.phase(Z))

    # Voltage across the resistor
    @property
    def voltage_resistor(self):
        I = self.Complex(self.current)
        V_R = I * self.R
        return self.Polar(V_R)

    # Voltage across the inductor
    @property
    def voltage_inductor(self):
        I = self.Complex(self.current)
        V_L = I * self._X_L
        return self.Polar(V_L)

    # Voltage across the capacitor
    @property
    def voltage_capacitor(self):
        I = self.Complex(self.current)
        V_C = I * self._X_C
        return self.Polar(V_C)

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
        return f'RLC Series Circuit with Resistance = {self.R}, Inductance = {self.X_L}, Capacitance = {self.X_C}'



#-------------------------------------------------------------------------------------------------------------------------------

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


#----------------------------------------------------------------------------------------------------------------------------



# RLC Parallel Resonance Circuit

import math
class RLC_parallel_resonance_circuit: 
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
        return 1 / (2 * math.pi *(math.sqrt(self._L * self._C)))

    def Q_factor(self):
        return self._R / (2 * math.pi * self.Resonance_f() * self._L)
    def Band_width(self):
        return self.Resonance_f() / self.Q_factor()
    def f1(self):
        return self.Resonance_f() - (self.Band_width() / 2)
    def f2(self):
        return self.Resonance_f() + (self.Band_width() / 2)        
    @staticmethod
    def Vc(I, Zp):
        return I * Zp   
    def Il(self, V_l):
        X_l = 2 * math.pi * self.Resonance_f() * self._L
        return V_l / X_l
    def Ic(self, V_c):
        X_c = 1 / (2 * math.pi * self.Resonance_f() * self._C)
        return V_c / X_c
    def __repr__(self):
        return f'{type(self).__name__} ({self.R}, {self.L}, {self.C})'
    def __str__(self):
        return f'RLC Resonance Parallel Circuit with Resistance: {self.R}, Inductance: {self.L}, Capacitance: {self.C}'


# ------------------------------------------------------------------------------------------------------------------------------

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
