#Controlled Power In the LightBulb class from Q3, add two methods: turn_on() and turn_off(). 
#These methods should toggle the self.on attribute, but only if the 
# light bulb isn't already in that state (e.g., cannot turn on if already True).

class lightbulb:

  def __init__(self, wattage, status):
    self.wattage = wattage
    self.on = status
    self.change()

  def change(self):
    if self.on == True:
      self.turn_off()
    else:
      self.turn_on()

  def turn_on(self):
    self.on = True
    print(f"The status of the bulb is ON (IF TRUE ) , OFF ( IF FALSE ) is : {self.on}")

  def turn_off(self):
    self.on = False
    print(f"The status of the bulb is ON (IF TRUE ) , OFF ( IF FALSE ) is : {self.on}")


bulb = lightbulb(100, True)


   

