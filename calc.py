from math import ceil

distance_to_boston_in_miles = 3051
extra_distance = 150
distance_to_boston_in_miles += extra_distance

average_lodging_cost_per_day_in_dollars = 150
number_of_people_per_lodging_room = 7

average_cost_of_flight_from_boston_to_seattle_in_dollars = 125
average_cost_per_gallon_of_gas_in_dollars = 2.25

average_cost_of_food_per_person_in_dollars_per_day = 7


def calculate_expenses(num_people, trip_length_in_days, car):
    expenses = {}

    gallons_of_gas_to_boston = gallons_of_gas(distance_to_boston_in_miles, car.miles_per_gallon)
    cost_of_gas_to_boston_in_dollars = average_cost_per_gallon_of_gas_in_dollars * gallons_of_gas_to_boston
    rental_cost_total = car.cost_per_day * trip_length_in_days

    num_cars = ceil(num_people / car.max_passengers)
    num_rooms = ceil(num_people / number_of_people_per_lodging_room)

    expenses["transportation"] = {}
    expenses["transportation"]["gas"] = cost_of_gas_to_boston_in_dollars * num_cars
    expenses["transportation"]["flights"] = average_cost_of_flight_from_boston_to_seattle_in_dollars * num_people
    expenses["transportation"]["car_rental"] = rental_cost_total * num_cars
    expenses["food"] = average_cost_of_food_per_person_in_dollars_per_day * num_people * trip_length_in_days
    expenses["lodging"] = (average_lodging_cost_per_day_in_dollars * (trip_length_in_days - 1)) * num_rooms

    expenses = flatten_dict(expenses)

    return expenses


def gallons_of_gas(miles, miles_per_gallon):
    return miles / miles_per_gallon


def reduce_dict(value):
    accumulator = 0
    if type(value) is dict:
        for key in value:
            accumulator += reduce_dict(value[key])
    else:
        accumulator += value
    return accumulator


def flatten_dict(input_dict):
    accumulator = {}
    for key in input_dict:
        value = input_dict[key]
        if type(value) is dict:
            new = flatten_dict(value)
            for flattened_key in new:
                flattened_value = new[flattened_key]
                accumulator[key + ": " + flattened_key] = flattened_value
        else:
            accumulator[key] = value
    return accumulator
