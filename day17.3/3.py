# 3. Limited Access Counter (Encapsulation, Constructor, Loop, Error Handling) 
# Challenge: Create a class that manages secure access attempts, limiting the number of failures.
# Requirements:
# Create a class AccessGate with a constructor taking a tuple of valid PINs.
# Encapsulate an attempt counter self._attempts_left (set to 3).
# Implement a method check_pin(entered_pin):
# Use a loop to compare the entered PIN against the valid PINs tuple.
# If the PIN is valid, print "Access Granted" and reset _attempts_left.
# If invalid, decrement _attempts_left.
# If _attempts_left hits 0, raise a custom exception, GateLockedError.
# Use a try...except block in your test code to demonstrate catching the GateLockedError.

class AccessGate:
    def __init__(self,valid_pins):
        self.valid_pins=valid_pins
        self._attempt_left=3
    def check_pin(self,entered_pin):
        self.entered_pin=entered_pin
        for i in self.valid_pins:
            if entered_pin==i:
                print("Access granted")
                self._attempt_left=3
            else:
                entered_pin != i
                self._attempt_left-=1
            if self._attempt_left==0:
                raise ("GateLockedErrorgate is locked")
            

gate = AccessGate((1234, 8888, 5555))

try:
    gate.check_pin(1111)  
    gate.check_pin(2222)  
    gate.check_pin(9999)  
    gate.check_pin(1234)  

except: 
    print("ERROR:")

