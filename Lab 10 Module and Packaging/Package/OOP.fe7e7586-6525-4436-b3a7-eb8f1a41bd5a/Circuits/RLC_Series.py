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
