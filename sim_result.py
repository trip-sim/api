from math import ceil

from calc import reduce_dict


class SimResult:
    def __init__(self, num_people, num_days, results):
        self.num_people = num_people
        self.num_days = num_days
        self.result = results
        self.total_cost = ceil(reduce_dict(results))
        self.cost_per_person = ceil(self.total_cost / num_people)

    def __repr__(self):
        return "[people: {}, days: {}, total cost: ${}, cost per person: ${}, result: {}]".format(self.num_people, self.num_days,
                                                                                  self.total_cost, self.cost_per_person, self.result)

    def to_tuple(self):
        return self.num_people, self.num_days, self.cost_per_person, self.total_cost
