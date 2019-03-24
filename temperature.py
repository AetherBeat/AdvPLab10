import re
"""Classes for working with Temperatures."""


class TemperatureError(Exception):
    """Error raised for invalid temperatures."""

    pass


class Temperature:
    """Represents a temperature.

    Temperatures are expressable in degrees Fahrenheit, degrees celsius,
    or Kelvins.
    """

    def __init__(self, degrees):
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
            TemperatureError: if degrees is not one of the specified
                                     forms
        """
        try:
            self.celsius = degrees
        except TypeError:
            raise TemperatureError

    @property
    def celsius(self):
        """Celsius value of the temperature"""
        return self._celsius

    @celsius.setter
    def celsius(self, celsius):
        """Sets the value of celsius"""
        if isinstance(celsius, str):
            check = str(re.sub('[^a-zA-Z]', '', celsius)).lower()
            if check != 'c' and check != 'k' and check != 'f' and check != '':
                raise TemperatureError
            else:
                celsius = float(re.sub('[a-zA-Z ]', '', celsius))
                if check == 'k':
                    celsius -= 273.15
                if check == 'f':
                    celsius = (celsius - 32) * 5/9
        elif not isinstance(celsius, (int, float)):
            raise TemperatureError
        self._celsius = celsius

    @property
    def fahrenheit(self):
        """Celsius value of the temperature"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, celsius):
        """Sets the value of celsius"""
        if isinstance(celsius, str):
            check = str(re.sub('[^a-zA-Z]', '', celsius)).lower()
            if check != 'c' and check != 'k' and check != 'f' and check != '':
                raise TemperatureError
            else:
                celsius = float(re.sub('[a-zA-Z ]', '', celsius))
                if check == 'k':
                    celsius -= 273.15
                if check == 'f':
                    celsius = (celsius - 32) * 5 / 9
        elif not isinstance(celsius, (int, float)):
            raise TemperatureError
        self._celsius = celsius

    @property
    def kelvin(self):
        """Celsius value of the temperature"""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, celsius):
        """Sets the value of celsius"""
        if isinstance(celsius, str):
            check = str(re.sub('[^a-zA-Z]', '', celsius)).lower()
            if check != 'c' and check != 'k' and check != 'f' and check != '':
                raise TemperatureError
            else:
                celsius = float(re.sub('[a-zA-Z ]', '', celsius))
                if check == 'k':
                    celsius -= 273.15
                if check == 'f':
                    celsius = (celsius - 32) * 5 / 9
        elif not isinstance(celsius, (int, float)):
            raise TemperatureError
        self._celsius = celsius

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
