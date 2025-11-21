# 5. Smart Home Device Manager 
# Challenge: Model smart devices in a home, ensuring secure IDs and simple, unified control.
# Requirements:
# Inheritance: Create a base class SmartDevice with a constructor that takes location.
# Encapsulation: In SmartDevice, strictly encapsulate the device ID (self.__device_id).
# Polymorphism: Create subclasses Light and Thermostat. Both must implement a method adjust_setting(value):
# Light sets self._brightness = value (0-100).
# Thermostat sets self._temperature = value (e.g., 60-80).
# Abstraction: In the base class SmartDevice, define a public method control(value) that simply calls the specialized adjust_setting(value) method. This allows a central controller to operate all devices using the single control() interface.

class SmartDevice:
    def __init__(self,location,device_id):
        self.location=location
        self.__device_id=device_id

    def get_device_id(self):
        return self.__device_id

    def adjust_setting(self):
        raise NotImplementedError

    def control(self,value):
       self.adjust_setting(value)

class Light(SmartDevice):
    def adjust_setting(self,value):
        self.value=value
        self._brightness=0

class Thermostat(SmartDevice):
    def adjust_setting(self,value):
        self.value=value
        self._temperature=80

smart=SmartDevice("hyd","12345")

light = Light("Living Room", "LGT-001")
thermo = Thermostat("Hallway", "THM-101")

light.control(75)
thermo.control(68)

print(light.get_device_id())
print(thermo.get_device_id())
print(light._brightness)
print(thermo._temperature)

