import random
from itertools import permutations

from utils import perform_operation, number_set


def generate_goal(num_set, possible_sets=None):
    root=False
    if  len(possible_sets)==0:
        root=True
    print("selected number: " + str(num_set))
    operands = random.sample(num_set, 2)
    print("operands: " + str(operands))

    if possible_sets is not None:
        copy_set=num_set.copy()
        while len(copy_set) < 6:
            copy_set.append(0)
        possible_sets.append(copy_set)

    while True:
        operation = random.choice(['+', '-', '*', '/'])
        solution = perform_operation(operands[0], operands[1], operation)
        if solution is not None and solution != 0:
            break

    print("operation: " + operation)
    print("solution: " + str(solution))

    if len(num_set) == 2:
        return solution

    new_set = [solution]
    for tok in num_set:
        if tok == operands[0]:
            operands[0] = None
        elif tok == operands[1]:
            operands[1] = None
        else:
            new_set.append(tok)

    while True:
        r=generate_goal(new_set, possible_sets)
        if r < 1000 or not root:
            break

    return r
