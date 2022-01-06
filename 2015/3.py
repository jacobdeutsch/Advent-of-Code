# Day 3
import pyperclip

directions = pyperclip.paste()

x = 0
y = 0

visited = {str(x) + ',' +str(y): 1} # create a dictionary to track places visited.  format is key: x,y with a value of 1 for visited.

for i in range(0, len(directions)): # iterate through each character of the clue
    if directions[i] == '^':
        y += 1
    elif directions[i] == 'v':
        y -= 1
    elif directions[i] == '>':
        x += 1
    elif directions[i] == '<':
        x -= 1
    
    visited[str(x) + ',' +str(y)] = 1

print('Santa went to ' + str(len(visited)) + ' houses.')


# Part 2

xSanta = 0
ySanta = 0
xRobo = 0
yRobo = 0

visited = {str(xSanta) + ',' +str(ySanta): 1} # create a dictionary to track places visited.  format is key: x,y with a value of 1 for visited.
visited = {str(xRobo) + ',' +str(yRobo): 1}

# Santa
for i in range(0, len(directions), 2): # iterate through each character of the clue
    if directions[i] == '^':
        ySanta += 1
    elif directions[i] == 'v':
        ySanta -= 1
    elif directions[i] == '>':
        xSanta += 1
    elif directions[i] == '<':
        xSanta -= 1
    
    visited[str(xSanta) + ',' +str(ySanta)] = 1

# Robo Santa
for i in range(1, len(directions), 2): # iterate through each character of the clue
    if directions[i] == '^':
        yRobo += 1
    elif directions[i] == 'v':
        yRobo -= 1
    elif directions[i] == '>':
        xRobo += 1
    elif directions[i] == '<':
        xRobo -= 1
    
    visited[str(xRobo) + ',' +str(yRobo)] = 1

print('Santa and Robo Santa went to ' + str(len(visited)) + ' houses.')