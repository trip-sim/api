from src.simulate import simulate
from src.vehicle import Vehicle
from src.visualizer import visualize

vehicles = [
    Vehicle("Rental Van", 7, 100, 20),
    Vehicle("Efficient Sedan", 5, 100, 40)
] * 20

miles_to_boston = 3061
average_cost_per_gallon_of_gas = 2
average_cost_per_night_at_hotel = 125
max_people_per_room = 5
average_cost_of_food_per_day_per_person = 7
ticket_cost_from_boston_to_seattle = 124

results = simulate(
    vehicles,
    miles_to_boston,
    average_cost_per_gallon_of_gas,
    average_cost_per_night_at_hotel,
    max_people_per_room,
    range(4, 14 + 1),
    range(7, 14 + 1),
    ticket_cost_from_boston_to_seattle,
    average_cost_of_food_per_day_per_person
)

visualize(results)
