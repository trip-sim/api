from calc import calculate_expenses
from sim_result import SimResult


def sim(people_range, day_range, car):
    results = []
    for people in people_range:
        for day in day_range:
            total_cost = calculate_expenses(people, day, car)
            results.append(SimResult(people, day, total_cost))
    return results
