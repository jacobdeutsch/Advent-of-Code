# Day 7
import pyperclip, re

instructions = pyperclip.paste().splitlines()  # read input into split line list
variables = {}  # create blank dictionary to start

# This is for part 2.  Remove or comment this line to run part 1 without overwriting and rerunning the code.
variables['b'] = 956

# Start by getting all the details per line, can be 1 - 3 variables, plus the operation.  Might be a number plus a
# variable. General forms "x OP y -> z", "123 -> x", "x -> y", "OP x -> y", note that OP is always cap and variables
# are always lowercase.

# Regex:  .search finds first instance, .findall will find all instances
targetVariableRegex = re.compile(r'->\s(\w+)')            # grabs target variable
operatorRegex = re.compile(r'([A-Z]+)')                      # grabs the operator (thanks to it being all caps)
firstVariableRegex = re.compile(r'(^[a-z0-9]+)\s')        # grabs the first variable.  Can be blank for NOT x -> y or a var or number
secondVariableRegex = re.compile(r'[A-Z]+\s([a-z0-9]+)')  # grabs the second variable, looks for anything after an all caps operator
#
# Regex Test:
# for line in instructions:
#     print('First Var %s  Second Var %s  Target Var %s  Operator %s' % (re.findall(firstVariableRegex, line), re.findall(secondVariableRegex, line), re.findall(targetVariableRegex, line), re.findall(operatorRegex, line)))


# Take in instruction line and return variables and operators AS STRINGS.  If empty return null string ''
def lineinfo(line):
    targetvariable = re.findall(targetVariableRegex, line)[0]
    operator = re.findall(operatorRegex, line)
    firstvariable = re.findall(firstVariableRegex, line)
    secondvariable = re.findall(secondVariableRegex, line)
    if operator == []:
        operator = 'ASSIGN'     # assignment operation is a little more explicit this way
    else:
        operator = operator[0]
    if firstvariable == []:
        firstvariable = ''
    else:
        firstvariable = firstvariable[0]
    if secondvariable == []:
        secondvariable = ''
    else:
        secondvariable = secondvariable[0]

    return firstvariable, secondvariable, targetvariable, operator


def iskeyindict(key, dic):          # checks if key (variable) is in the dictionary
    if key in dic:
        return True
    else:
        return False


for rounds in range(0, len(instructions)):  # feeling lazy so i'm just going to run this throuhg the entire list once for each line since that should definitely run them all
    print('Starting round ' + str(rounds + 1) + ' of ' + str(len(instructions)) + '.')

    for line in instructions:
        firstVariable, secondVariable, targetVariable, operator = lineinfo(line)
        if iskeyindict(targetVariable, variables):
            continue    # if the target variable is already assigned we can skip this entire iteration and move to the next line

        #find function, check if function has variables needed to run, if not continue, if so, execute
        match operator:
            case 'ASSIGN':
                if firstVariable.isdigit():
                    variables[targetVariable] = int(firstVariable)
                elif iskeyindict(firstVariable, variables):
                    variables[targetVariable] = variables[firstVariable]

            case 'NOT':
                if iskeyindict(secondVariable, variables):
                    variables[targetVariable] = ~ variables[secondVariable]

            case 'AND':
                if firstVariable.isdigit() and iskeyindict(secondVariable, variables):
                    variables[targetVariable] = int(firstVariable) & variables[secondVariable]
                elif iskeyindict(firstVariable, variables) and iskeyindict(secondVariable, variables):
                    variables[targetVariable] = variables[firstVariable] & variables[secondVariable]

            case 'OR':
                if iskeyindict(firstVariable, variables) and iskeyindict(secondVariable, variables):
                    variables[targetVariable] = variables[firstVariable] | variables[secondVariable]

            case 'LSHIFT':
                if iskeyindict(firstVariable, variables):
                    variables[targetVariable] = variables[firstVariable] << int(secondVariable)

            case 'RSHIFT':
                if iskeyindict(firstVariable, variables):
                    variables[targetVariable] = variables[firstVariable] >> int(secondVariable)

        if iskeyindict(targetVariable, variables) and variables[targetVariable] < 0:
            variables[targetVariable] = variables[targetVariable] % 2 ** 16


print(variables)
print('The value of wire a is: %d.' % variables['a'])


