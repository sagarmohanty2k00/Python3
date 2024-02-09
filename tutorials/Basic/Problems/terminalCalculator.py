def calculate(exp):
    _list = exp.split()

    if _list[1] == '+':
        return (int(_list[0]) + int(_list[2]))

    elif _list[1] == '-':
        return (int(_list[0]) - int(_list[2]))

    elif _list[1] == '*':
        return (int(_list[0]) * int(_list[2]))

    else:
        return (int(_list[0]) / int(_list[2]))


def calculatePlusAndMinus(exp):
    _list = exp.split()

    _ans = int(_list[0])
    _operands = []
    _operators = []

    for idx in range(1, len(_list)):
        if idx % 2 == 0: # even
            _operands.append(int(_list[idx]))
        else:
            _operators.append(_list[idx])

    for idx in range(len(_operators)):
        if _operators[idx] == '+':
            _ans += _operands[idx]
        else:
            _ans -= _operands[idx]

    return _ans

while True:
    expression = input(":") # 2 + 3 => ['2', '+', '3']
    print(calculatePlusAndMinus(expression))