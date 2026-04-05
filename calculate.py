'''calculate'''
def calc(a, op, b) -> int:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return 10000
        return a / b
