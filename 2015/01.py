# Day 1 Part 1
import pyperclip # just going to get the clue from the clipboard

clue = pyperclip.paste() # pasting clue into clue variable.

floor = 0 # set floor to 0 to start
for i in range(0, len(clue)): # iterate through each character of the clue, adding 1 to floor for each ( and subtracting for every )
    if clue[i] == '(':
        floor += 1
    elif clue[i] == ')':
        floor -= 1

print('Santa ends up on floor ' + str(floor) + '.')  # print out the answer


# Day 1 Part 2
floor = 0 # reset floor to 0 or else you end up with the wrong number...
for i in range(0, len(clue)): # iterate through each character of the clue, adding 1 to floor for each ( and subtracting for every )
    if clue[i] == '(':
        floor += 1
    elif clue[i] == ')':
        floor -= 1
    
    if floor < 0:
        print('Santa first ends up in the basement at position ' + str(i + 1) + '.')
        break
