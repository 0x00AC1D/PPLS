from copy import deepcopy
from itertools import combinations

    def calculate_fitness(self):
        number_of_conflicts = 0
        classes = deepcopy(self.classes)
        
        while classes:
            x = classes[0]
            potential_conflict_group = filter(lambda z: (x.timeslot.day == z.timeslot.day and 
                                                         x.course.subject.department == z.course.subject.department and 
                                                         x.course.subject.program == z.course.subject.program and 
                                                         x.course.subject.semester == z.course.subject.semester and 
                                                         x.course.group.id == z.course.group.id and x.id != z.id), classes)

            classes = list(set(classes).difference(potential_conflict_group))
            number_of_conflicts += sum(x.timeslot.start_time in range(y.timeslot.start_time, y.timeslot.end_time) or
                                    y.timeslot.start_time in range(x.timeslot.start_time, x.timeslot.end_time) 
                                    for x, y in combinations(potential_conflict_group))

        # Return a normalized fitness value between [0, 1]
        return 1 / (number_of_conflicts + 1)