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
        # TODO Handle kelvin and fahrenheit
        self.celsius = degrees

    @property
    def celsius(self):
        """Celsius value of the temperature"""
        return self.temperature_celsius

    @celsius.setter
    def celsius(self, celsius):
        """Sets the value of celsius"""
        if isinstance(celsius, str):
            celsius = float(re.sub('[a-zA-Z ]', '', celsius))
        elif not isinstance(celsius, (int, float)):
            raise TemperatureError
        self.temperature_celsius = celsius



    @classmethod
    def average(cls, temperatures):
        """Compute the average of a list of temperatures.

        Args:
            temperatures: a list of Temperature objects
        Returns:
            a Temperature object with average (mean) of the given temperatures

        """
        pass
