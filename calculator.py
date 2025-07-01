# simple calculator for testing the git versions
def calculator(a, b):
    return a + b, a * b

# second commit
def calculator1(a, b):
    add = a + b
    multiply = a * b
    divide = a / b if b != 0 else 'undefined'
    return add, multiply, divide

