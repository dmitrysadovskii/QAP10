operators = {"**": 0, "*": 1, "/": 1, "+": 2, "-": 2}

priorities = sorted(set(operators.values()))


def get_min_index(lst: list, operators_list):
    min_operator_index = -1

    if True in (operator in lst for operator in operators_list):
        for operator in operators_list:
            if operator in lst:
                index = lst.index(operator)

                if index < min_operator_index or min_operator_index == -1:
                    min_operator_index = index

    return min_operator_index


def process_expression(expression):
    lst = expression.split()
    while len(lst) > 1:
        for priority in priorities:
            index_oper = 0
            while index_oper > -1:
                priority_operators = {op for op in operators if operators[op] == priority}
                index_oper = get_min_index(lst, priority_operators)

                if index_oper > -1:
                    operation_result = calculate(lst[index_oper], lst[index_oper - 1], lst[index_oper + 1])
                    lst[index_oper - 1] = operation_result
                    lst.pop(index_oper + 1)
                    lst.pop(index_oper)

    return lst[0]


def calculate(operation, a, b):
    result = float(0)
    a = float(a)
    b = float(b)
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    elif operation == "**":
        result = a ** b

    return result


exp = input("Enter expression: ")

print(process_expression(exp))
