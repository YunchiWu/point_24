import input
import calculate

def main() -> None:
    eq_list = input.input_seq()
    op_list = input.op_seq()
    for eq in eq_list:
        a, b, c, d = eq
        for op in op_list:
            # 1. ((a op1 b) op2 c) op3 d
            if calculate.calc(calculate.calc(calculate.calc(a, op[0], b), op[1], c), op[2], d) == 24:
                print(f"(({a}{op[0]}{b}){op[1]}{c}){op[2]}{d}")
                return
            # 2. (a op1 b) op2 (c op3 d)
            if calculate.calc(calculate.calc(a, op[0], b), op[1], calculate.calc(c, op[2], d)) == 24:
                print(f"({a}{op[0]}{b}){op[1]}({c}{op[2]}{d})")
                return
            # 3. (a op1 (b op2 c)) op3 d
            if calculate.calc(calculate.calc(a, op[0], calculate.calc(b, op[1], c)), op[2], d) == 24:
                print(f"({a}{op[0]}({b}{op[1]}{c})){op[2]}{d}")
                return
            # 4. a op1 ((b op2 c) op3 d)
            if calculate.calc(a, op[0], calculate.calc(calculate.calc(b, op[1], c), op[2], d)) == 24:
                print(f"{a}{op[0]}(({b}{op[1]}{c}){op[2]}{d})")
                return
            # 5. a op1 (b op2 (c op3 d))
            if calculate.calc(a, op[0], calculate.calc(b, op[1], calculate.calc(c, op[2], d))) == 24:
                print(f"{a}{op[0]}({b}{op[1]}({c}{op[2]}{d}))")
                return
    print("No solution")

if __name__ == '__main__':
    main()
