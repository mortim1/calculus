import sys
import shlex

def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

# ------------------------------------------------------------------------------

def eval_(parsed):
    stack = []



    for x in parsed:
        if x.isnumeric() or isfloat(x):
            stack.append(x)
        else:
            remainder = stack[-2:]
            del stack[-2:]
            if x == "^":
                result = eval(str(remainder[0]) + "**" + str(remainder[1]))
            else:
                result = eval(str(remainder[0]) + str(x) + str(remainder[1]))
            stack.append(result)
    
    return stack[0]

# ------------------------------------------------------------------------------

def parse(calculus):
    numbers = []
    operators = []

    for x in calculus:
        if x.isnumeric() or isfloat(x):
            numbers.append(x)

        elif x == "+" or x == "-":
            
            if operators[:1] == ["*"] or operators[:1] == ["/"] or operators[:1] == ["^"]:
                i = 0
                while i < len(operators):
                    numbers.append(operators.pop(i))
                    i+1
                operators.append(x)

            elif operators[:1] == [x]:
                operators.append(x)
                numbers.append(operators.pop(0))
            else:
                operators.append(x)

        elif x == "*" or x == "/" or x == "^":

            if operators[:1] == ["^"]:
                i = 0
                while i < len(operators):
                    numbers.append(operators.pop(i))
                    i+1
                operators.append(x)
            else:
                operators.insert(0, x)            
            
        else:
            return sys.exit("calculus: Cannot parsing this expression.")

    return numbers + operators


# ------------------------------------------------------------------------------


def run():
    print("calculus - calculator written in Python by mortim\n")
        
    n = input("calculus) ")

    while n != "quit":
        calc = shlex.shlex(n, punctuation_chars=True)
        calc.wordchars = calc.wordchars.replace("-", "").replace("/", "").replace("*", "")
        l_calc = list(calc)

        if l_calc[:1] == ['-']:
            l_calc.pop(0)
            l_calc[0] = "-"+l_calc[0]

        parsed = parse(l_calc)
        evaluated = eval_(parsed)

        print(evaluated)
        n = input("calculus) ")


# ------------------------------------------------------------------------------

run()
