from utils import perform_operation


def best_solution(goal: object, selected_numbers: object, dic: object, ops: object = None) -> object:
    if ops is None:
        ops = []
    for tok in selected_numbers:
        if tok == goal:
            op = ops[0]
            if str(op) not in dic:
                dic[str(op)] = len(ops)
            else:
                x = dic[str(op)]
                if x > len(ops):
                    dic[str(op)] = len(ops)

            return ops

    for i in range(0, len(selected_numbers) - 1):
        for j in range(i + 1, len(selected_numbers)):
            for op in ["*", "/", "+", "-"]:
                val = perform_operation(selected_numbers[i], selected_numbers[j], op)
                if (val is None) or (val == selected_numbers[i]) or (val == selected_numbers[j]) or (val == 0):
                    continue

                new_number = selected_numbers.copy()
                new_number.pop(max(i, j))
                new_number.pop(min(i, j))
                new_number.append(val)

                ops_new = ops.copy()
                ops_new.append([i, j, op])

                best_solution(goal, new_number, dic, ops_new)

            for op in ["/", "-"]:
                val = perform_operation(selected_numbers[j], selected_numbers[i], op)
                if (val is None) or (val == selected_numbers[i]) or (val == selected_numbers[j]):
                    continue

                new_number = selected_numbers.copy()
                new_number.pop(max(i, j))
                new_number.pop(min(i, j))
                new_number.append(val)

                ops_new = ops.copy()
                ops_new.append([j, i, op])

                best_solution(goal, new_number, dic, ops_new)


class Solver:
    def __init__(self, game):
        self.evaluations: object = dict()
        best_solution(game.goal, game.numbers, self.evaluations)
        print("ev1:" + str(self.evaluations))

    def evaluate(self, move):
        print("ev2:"+str(self.evaluations))
        #move=move_to_operation(m)
        print("str([move.op1, move.op2, move.op]):"+str([move.op1, move.op2, move.op]))
        if str([move.op1, move.op2, move.op]) in self.evaluations:
            val = self.evaluations[str([move.op1, move.op2, move.op])]
        else:
            return 0

        if val == 1:
            return 2000
        if val == 2:
            return 900
        if val == 3:
            return 700
        if val == 4:
            return 500
        if val == 5:
            return 300
        if val == 6:
            return 100

        return 0
