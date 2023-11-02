import random

from forcebrute_solver import Solver
from game_creator import generate_goal
from move import move_to_operation
from utils import number_set, perform_operation


class Game:

    def __init__(self):
        self.goal = None
        self.numbers = None
        self.score = 0
        self.step = 0
        self.reset()

    def reset(self):
        sel_numbers: object = random.sample(number_set, 6)
        pos_sets = []
        while True:
            goal = generate_goal(sel_numbers, pos_sets)
            if goal not in sel_numbers:
                break

        self.goal = goal

        while True:
            self.numbers = random.sample(pos_sets, 1)[0]
            if goal not in self.numbers:
                break

        self.numbers.sort()
        self.score = 0
        self.step = 0

    def play_step(self, move):

        m=move_to_operation(move)
        s = Solver(self)
        reward = s.evaluate(m)

        print(str(self.numbers))
        print(str(m.op1))
        print(str(m.op2))

        if(m.op1>m.op2):
            n1 = self.numbers.pop(m.op1)
            n2 = self.numbers.pop(m.op2)
        else:
            n2 = self.numbers.pop(m.op2)
            n1 = self.numbers.pop(m.op1)
        val = perform_operation(n1, n2, m.op)

        game_over = False
        self.step += 1

        if val is None or val == 0 or val==n1 or val==n2:
            reward = -1000
            game_over = True
            self.score = 0
            self.numbers.append(n1)
            self.numbers.append(n2)

        elif val == self.goal:
            game_over = True
            self.score = 1000 - self.step * 100
            self.numbers.append(val)
        else:
            self.numbers.append(val)

        while len(self.numbers) < 6:
            self.numbers.append(0)

        self.numbers.sort()

        return reward, game_over, self.score



# Select 6 random numbers from the set
# selected_numbers: object = random.sample(number_set, 6)
# selected_numbers = [6, 76, 0, 12, 0, 10]
# possible_sets = []
# result = generate_goal(selected_numbers, possible_sets)
# result = 912
# d = {}
# best_solution(result, selected_numbers, dic=d)
# Print the selected numbers and the target goal
# print("Selected Numbers:", str(selected_numbers))
# print("possible_sets:", str(possible_sets))
# print("Target Goal:", int(result))
# print("D:", str(d))
