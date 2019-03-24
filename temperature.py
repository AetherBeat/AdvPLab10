"""Classes for working with Temperatures.

Author: Tyler Baker
Class: CSI-260-02
Assignment: Week 10 Lab
Due Date: March 25, 2019 11:00 AM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import re


class TemperatureError(Exception):
    """Error raised for invalid temperatures."""

    pass


class Temperature:
    """Represents a temperature.

    Temperatures are expressable in degrees Fahrenheit, degrees celsius,
    or Kelvins.
    """

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees.

        Args:
            degrees, which can be one of the following:
                (1) a number, or a string containing a number
                    in which case it is interpreted as degrees celsius
                (2) a string containing a number followed by one of the
                    following symbols:
                       C, in which case it is interpreted as degrees celsius
                       F, in which case it is interpreted as degrees Fahrenheit
                       K, in which case it is interpreted as Kelvins

        Raises:
            TemperatureError: if degrees is not one of the specified forms

        """
        try:
            self.celsius = degrees
        except TypeError:
            raise TemperatureError

    @property
    def celsius(self):
        """Celsius value of the temperature."""
        return self._celsius

    @celsius.setter
    def celsius(self, celsius):
        """Set the value of celsius."""
        if isinstance(celsius, str):
            check = str(re.sub('[^a-zA-Z]', '', celsius)).lower()
            if check != 'c' and check != 'k' and check != 'f' and check != '':
                raise TemperatureError
            else:
                celsius = float(re.sub('[a-zA-Z]', '', celsius))
                if check == 'k':
                    celsius -= 273.15
                if check == 'f':
                    celsius = (celsius - 32) * 5/9
        elif not isinstance(celsius, (int, float)):
            raise TemperatureError
        self._celsius = celsius

    @property
    def fahrenheit(self):
        """Fahrenheit value of temperature."""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        """Set the value of celsius."""
        if isinstance(fahrenheit, str):
            check = str(re.sub('[^a-zA-Z]', '', fahrenheit)).lower()
            if check != 'c' and check != 'k' and check != 'f' and check != '':
                raise TemperatureError
            else:
                fahrenheit = float(re.sub('[a-zA-Z]', '', fahrenheit))
                if check == 'k':
                    fahrenheit = ((fahrenheit - 273.15) * 9/5) + 32
                if check == 'c':
                    fahrenheit = (fahrenheit * 9/5) + 32
        elif not isinstance(fahrenheit, (int, float)):
            raise TemperatureError
        self._celsius = (fahrenheit - 32) * 5/9

    @property
    def kelvin(self):
        """Convert Celsius to kelvin and return it."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, kelvin):
        """Set the value of celsius."""
        if isinstance(kelvin, str):
            check = str(re.sub('[^a-zA-Z]', '', kelvin)).lower()
            if check != 'c' and check != 'k' and check != 'f' and check != '':
                raise TemperatureError
            else:
                kelvin = float(re.sub('[a-zA-Z]', '', kelvin))
                if check == 'c':
                    kelvin += 273.15
                if check == 'f':
                    kelvin = (kelvin - 32) * 5/9 + 273.15
        elif not isinstance(kelvin, (int, float)):
            raise TemperatureError
        self._celsius = kelvin - 273.15

    @classmethod
    def average(cls, temperatures):
        """Compute the average of a list of temperatures.

        Args:
            temperatures: a list of Temperature objects
        Returns:
            a Temperature object with average (mean) of the given temperatures

        """
        temp_sum = 0
        for temperature in temperatures:
            temperature = temperature.celsius
            temp_sum += temperature
        return Temperature(temp_sum/len(temperatures))
