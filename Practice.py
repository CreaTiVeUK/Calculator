import math
import sys


def start(filename=None):
    if filename is None:
        calculator()
    elif filename == "statements":
        processfile1(filename)
    else:
        processfile2(filename)


def calculator():
    expression = userinput()
    print(eval(expression))


def userinput():
    operation = input('Enter operation ')
    number1 = input('Enter 1st number ')
    number2 = input('Enter 2nd number ')
    expression = number1 + operation + number2
    return expression


def processfile1(filename):
    file = loadfile(filename)
    result = []
    for i in file:
        values = i.split()
        values = [operation.replace("x", "*") for operation in values]
        expression = eval(values[2] + values[1] + values[3])
        result.append(expression)
        print(expression)
    print_total(result)


def processfile2(filename):
    file = loadfile(filename)
    result = []
    i = 0
    while i <= len(file):
        values = file[i].split()
        current_line = i
        if "calc" in values:
            values = [operation.replace("x", "*") for operation in values]
            expression = math.floor(eval(values[3] + values[2] + values[4]))
            to_append = "goto " + str(expression)
            i = expression-1
        else:
            to_append = "goto " + values[1]
            i = int(values[1])-1
        if to_append in result:
            print("Statement is \"" + to_append + "\" and line number is " + str(current_line))
            sys.exit()
        result.append(to_append)


def loadfile(filename):
    with open(filename, 'r') as f:
        file = f.read()
        f.close()
    return file.split('\n')


def print_total(result):
    print('Total is: ', sum(result))


if __name__ == "__main__":
    start("statements2")
