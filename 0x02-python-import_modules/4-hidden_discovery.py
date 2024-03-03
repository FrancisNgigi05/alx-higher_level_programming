#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    modules = dir(hidden_4)

    for function in modules:
        if not function.startswith("__"):
            print(function)
