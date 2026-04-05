'''input'''
def input_seq() -> list:
    a, b, c, d = (int(x) for x in input().split(' '))
    eq = [a, b, c, d]
    eq_list = []
    for i in range(len(eq)):
        for j in range(len(eq)):
            if j != i:
                for k in range(len(eq)):
                    if k != j and k != i:
                        for l in range(len(eq)):
                            if l != k and l != j and l != i:
                                eq_list.append([eq[i], eq[j], eq[k], eq[l]])
    return eq_list

def op_seq() -> list:
    op_list = []
    for op1 in ['+', '-', '*', '/']:
        for op2 in ['+', '-', '*', '/']:
            for op3 in ['+', '-', '*', '/']:
                op_list.append([op1, op2, op3])
    return op_list
