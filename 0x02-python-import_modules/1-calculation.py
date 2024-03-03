#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    operator = None

    func_list = [add, sub, mul, div]

    for function in func_list:
        if function == add:
            operator = "+"
        elif function == sub:
            operator = "-"
        elif function == mul:
            operator = "*"
        elif function == div:
            operator = "/"
        else:
            print("Invalid")
        print("{} {} {} = {}".format(a, operator, b, function(a, b)))
