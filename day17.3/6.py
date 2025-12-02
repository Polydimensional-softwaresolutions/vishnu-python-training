# Temperature Converter Abstraction (Encapsulation, Abstraction, Error Handling) 
# Challenge: Design a class to handle temperature conversion, hiding the internal unit used for storage.
# Requirements:
# Create a class ThermoConverter.
# Encapsulate the internal temperature storage as Celsius (self._temp_celsius).
# Implement a public method set_temp_f(temp_f) that converts the Fahrenheit input to Celsius before storing it in _temp_celsius.
# Implement a public method get_temp_k() that converts the Celsius storage to Kelvin ($\text{K} = \text{C} + 273.15$) before returning it.
# Use Error Handling within set_temp_f to raise a ValueError if the input is below absolute zero ($-459.67^\circ\text{F}$).

class ThermoConverter:
    def __init__(self,temp_celcius):
        self._temp_celcius=temp_celcius
    def set_temp_f(self,temp_f):
        if temp_f < -459.67:
            raise ValueError
    def get_temp_k(self):
        return self._temp_celcius
    
    doubt