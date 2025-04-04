# uwa/wave.py

from numpy import sin, cos, pi
from math import radians

class AcousticWave:
    """
    A class to represent an underwater acoustic wave.

    Attributes:
        frequency (float): Frequency of the wave in Hz.
        speed (float): Speed of sound in water in m/s (default 1500 m/s).
        bw (float): θ3dB, 3 dB beamwidth in ° (default 7°). 
    """

    def __init__(self, frequency, speed=1500, bw = 7):
        #assign inputs to self
        self.frequency = frequency
        self.speed = speed
        self.bw = bw
        
        #initialisation calculations:
        self.wl = self.wavelength()
        self.k = self.wave_number()
        self.ar = self.active_radius()
        self.rnf = self.nearfield_distance()

    def wavelength(self):
        """Calculate the wavelength λ = c / f"""
        return self.speed / self.frequency

    def wave_number(self):
        """Calculate the wave number k = 2π / λ"""
        return 2 * pi / self.wavelength()

    def active_radius(self):
        """Calculates the active radius of a round transducer in ster"""
        return 3.2 / (self.wave_number() * sin(radians(self.bw /2) ))
        
    def nearfield_distance(self):
        """Calculate the acoustic near-field distance in m"""
        return pi * self.active_radius()**2 / (4 * self.wavelength())

def deadzone(d, speed,q, tau):
    """
    Calculate the distance from the bottom at which there is bias

    Parameters:
        d (float or integer): Bottom Depth in m
        speed (float or integer): Ambient sound speed in m/s
        q (float or integer): slope of the seafloor in °
        tau (float or integer): pulse duration in s

    Returns:
        Distance from the bottom where there is bias in m
        
    """
    return (d / sin(radians(90 - q)) - d) + speed * tau / 2