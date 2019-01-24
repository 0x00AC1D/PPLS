from copy import deepcopy
from random import randint
from itertools import combinations

class Class:
    """Dummy Class, for testing timeslot collision"""
    def __init__(self):
        self.a = randint(1, 10)
        self.b = randint(1, 10)
        self.start = randint(0, 10)
        self.end = self.start + randint(5, 15)

unique_classes = [Class() for _ in range(1000)]
classes = deepcopy(unique_classes)
total_conflicts = 0

# maximum number of iterations will be the product of possibilities of all attributes
# in my case 100 since both Class().a and Class().b can hold 10 different values
while classes:
    y = classes[0]
    potential_conflict_group = set(filter(lambda x: x.a == y.a and x.b == y.b, classes))
    classes = list(set(classes).difference(potential_conflict_group))

    total_conflicts += sum(x.start in range(y.start, y.end+1) or y.start in range(x.start, x.end+1)
                                    for x, y in combinations(potential_conflict_group, 2))

print(total_conflicts)