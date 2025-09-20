distance=int(input("Total distance travelled:"))
fuel_consumed=int(input("fuel consumed in litres:"))
price_consumed=int(input("price of fuel per litre:"))

mileage= distance / fuel_consumed
total_fuel_cost=price_consumed * fuel_consumed
cost_per_km=total_fuel_cost / distance

print(f"mileage (km per liter):{mileage:.2f} ")
print(f"total_fuel_cost:{total_fuel_cost:.2f} ")
print(f"cost_per_kilo meter:{cost_per_km:.2f} ")