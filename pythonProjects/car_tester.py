'''from car import Car # import car class

cars_list = []

with open("cars.txt") as file:
    for line in file: 
        car_data = line.split()
        car_color = car_data[0]
        car_engine = car_data[1]
        car_gas_tank = int(car_data[2])
        car_odometer = int(car_data[3])

        car = Car(car_color, car_engine, car_gas_tank, car_odometer)
        cars_list.append(car)

print(car[0])
print(car[1])'''

from car import Car  


cars_list = []
with open('cars.txt') as file:
    for line in file:
        car_data = line.split()
        car_color = car_data[0]
        car_engine_type = car_data[1]
        car_gas_tank = int(car_data[2])  
        car_odometer = int(car_data[3])  

        car = Car(car_color, car_engine_type, car_gas_tank, car_odometer)
        cars_list.append(car)

print(f"First car: {cars_list[0]}")
cars_list[0].drive()  
print(f"First car gas tank after driving: {cars_list[0].get_gas_tank()} gallons")
print(f"First car odometer after driving: {cars_list[0].get_odometer()} miles")


print(f"Second car: {cars_list[1]}")
cars_list[1].drive() 
print(f"Second car gas tank after driving: {cars_list[1].get_gas_tank()} gallons")
print(f"Second car odometer after driving: {cars_list[1].get_odometer()} miles")
