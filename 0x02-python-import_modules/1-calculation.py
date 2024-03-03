#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    operator = None

    func_list = [add, sub, mul, div]

    for i in func_list:
        if i == add:
            operator = "+"
        elif i == sub:
            operator = "-"
        elif i == mul:
            operator = "*"
        elif i == div:
            operator = "/"
        else:
            print("Invalid")
        print("{} {} {} = {}".format(a, operator, b, i(a, b)))
