# DESCRIPTION:
# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
#
# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7
def basic_op(operator, value1, value2):
    if operator=='+':
        sum = value2 + value1
    elif operator=='-':
        sum = value1 - value2
    elif operator == '*':
        sum = value1* value2
    elif operator== '/':
        sum = value1 / value2
    return int(sum)
#print(basic_op('*', 10, 7))

