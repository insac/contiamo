mapmove = ["1+2", "1+3", "1+4", "1+5", "1+6", "2+3", "2+4", "2+5", "2+6", "3+4", "3+5", "3+6", "4+5", "4+6", "5+6",
           "1*2", "1*3", "1*4", "1*5", "1*6", "2*3", "2*4", "2*5", "2*6", "3*4", "3*5", "3*6", "4*5", "4*6", "5*6",
           "1/2", "1/3", "1/4", "1/5", "1/6", "2/1", "2/3", "2/4", "2/5", "2/6", "3/1", "3/2", "3/4", "3/5", "3/6",
           "4/1", "4/2", "4/3", "4/5", "4/6", "5/1", "5/2", "5/3", "5/4", "5/6", "6/1", "6/2", "6/3", "6/4", "6/5",
           "1-2", "1-3", "1-4", "1-5", "1-6", "2-1", "2-3", "2-4", "2-5", "2-6", "3-1", "3-2", "3-4", "3-5", "3-6",
           "4-1", "4-2", "4-3", "4-5", "4-6", "5-1", "5-2", "5-3", "5-4", "5-6", "6-1", "6-2", "6-3", "6-4", "6-5"]


class Move:

    def __init__(self, o1, o2, op):
        self.op1 = o1
        self.op2 = o2
        self.op = op


def move_to_operation(move: object) -> object:
    print("Move:"+str(move))
    operation = mapmove[move];
    r= Move(int(operation[0]) - 1, int(operation[2]) - 1, operation[1])
    print("r:"+str(operation))
    return r


def operation_to_move(o1: int, o2:int, op:str) -> int:
    a=str(o1+1)
    b=str(o2+1)
    if o1>o2 and (op=='+' or op=='*'):
        a=str(o2+1)
        b=str(o1+1)

    return mapmove.index(a+str(op)+b)

