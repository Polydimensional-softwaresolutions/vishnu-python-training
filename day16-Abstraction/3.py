# 3. Abstracting Complex Logic with a Single Function 
# Challenge: Create a GPS class that abstracts the messy details of location finding into one clean method.
# Requirements:
# Define a class GPS with a constructor that initializes self.current_location (e.g., "Park").
# Define a method _process_satellites() that simply prints: "--- Receiving data from 12 satellites ---"
# Define a public method find_route(destination):
# It must call _process_satellites().
# It must print: "Calculating shortest path from [current_location] to [destination]."
# It must print: "Route ready."
# Create a GPS object and call find_route("Museum"). The user only needs to provide the destination.

class GPS:
    def __init__(self,current_location):
        self.current_location=current_location

    def _process_satellites(self):
        print("--- Receiving data from 12 satellites ---")
    
    def find_route(self,destination):
        self.destination=destination

gps=GPS("park")
gps._process_satellites()
gps.find_route("museum")
print(f"calculating shortest path from {gps.current_location} to {gps.destination}")
print("route ready")
        