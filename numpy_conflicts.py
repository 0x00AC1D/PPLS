import numpy as np
from random import randint
from pprint import pprint

def assign_var_len_tslots(row):
    duration = randint(2,6)
    start = randint(0, 25-duration)
    row = row.reshape((1, 26))
    row[:, start:start+duration] = 1
    return row

def assign_fix_len_tslots(row):
    row = row.reshape((1, 5))
    row[:] = 1
    return row

def conflicts_within_array(size, apply_func):
    class_tslots = np.zeros(size)
    np.apply_along_axis(apply_func, 1, class_tslots)
    conflicts = np.triu(class_tslots.dot(class_tslots.T), 1)
    num_of_conflicts = np.count_nonzero(conflicts)
    pprint(conflicts)
    return num_of_conflicts

print("array(15, 56) random lengths 2-5 inclusive conflicts")
print(conflicts_within_array((15, 26), assign_var_len_tslots))

print("\narray(15, 5) fixed length 5 conflicts")
print("sanity check should be equal to 15*14/2 == 105")
print(conflicts_within_array((15, 5), assign_fix_len_tslots))