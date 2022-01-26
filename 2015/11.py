# Day 11

#puzzleInput = 'hxbxwxba' # part one initial password
puzzleInput = 'hxbxxyzz' # part 2 initial password (and answer to part 1)

passlist = []


def listtostring(input):        # takes the list of string numbers and makes it into the string
    output = ''
    for i in input:
        output += chr(i + 96)

    return output


def incrementpassword(input):
    input[len(input) - 1] += 1
    if 27 not in input:
        return input

    # so this happens if 27 is in input
    for i in range(len(input) - 1, -1, -1):
        if input[i] == 27:
            input[i] = 1
            if i != 0:
                input[i - 1] += 1

    return input


def isValid(input):     # takes in list of string numbers and verifies that it is valid

    if 9 in input or 15 in input or 12 in input:    # first check for i o and l (9, 15 and 12)
        return False

    straights = False
    for i in range(len(input) - 2):       # check for straight of 3 characters
        if input[i] == input[i + 1] - 1 and input[i + 1] == input[i + 2] - 1:
            straights = True
            break
    if straights == False:
        return False

    doubles = 0  # counter to check for doubles
    skip = False    # creating a skip variable to avoid seeing 'aaa' as 2 sets of doubles
    for i in range(len(input) - 1):     # check for 2 sets of doubled characters
        if skip == True:
            skip = False
            continue
        if input[i] == input[i + 1]:
            doubles += 1
            skip = True
    if doubles < 2:
        return False

    return True


for char in puzzleInput:
    passlist.append(ord(char) - 96)       # makes list with numbers in place of characters with a = 1 to z = 26

passlist = incrementpassword(passlist)  #run first increment and then do the while loop
while isValid(passlist) == False:    # while the new password is not valid, increment
    passlist = incrementpassword(passlist)

password = listtostring(passlist)
print(password)
