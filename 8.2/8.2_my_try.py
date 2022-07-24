def evaluate(expression):
    rpn = expression.split(",")
    stack = []
    intermediate_values = []

    operations = {"+": lambda x, y: int(x) + int(y), "-": lambda x, y: int(x) - int(y),
                  "/": lambda x, y: int(x) // int(y), "*": lambda x, y: int(x) * int(y)}

    for val in rpn:
        if val.isnumeric():
            stack.append(val)

        elif len(stack) == 2:
            intermediate_values.append(operations[val](stack.pop(), stack.pop()))
        else:
            intermediate_values.append(operations[val](stack.pop(), intermediate_values[-1]))

    return intermediate_values[-1]

expression = "3,4,+,2,*,1,+"
evaluate(expression)


# print(int("3") + int("4"))