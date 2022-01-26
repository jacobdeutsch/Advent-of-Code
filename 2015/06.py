# Day 6

import pyperclip, re
import numpy as np

instructions = pyperclip.paste().splitlines()  # read input into split line list

lights = np.zeros((1000, 1000))  # create light array with 0 meaning off, 1 meaning on

numRegex = re.compile(r'[0-9]+')

def isinrange(x, y, lowx, lowy, highx, highy):
    if lowx <= x <= highx:
        if lowy <= y <= highy:
            return True
    return False


def onoff(state, lowx, lowy, highx, highy):
    for i in range(0, lights.shape[0]):
        for j in range(0, lights.shape[1]):
            if isinrange(i, j, lowx, lowy, highx, highy):
                lights[i][j] = state


def toggle(lowx, lowy, highx, highy):
    for i in range(0, lights.shape[0]):
        for j in range(0, lights.shape[1]):
            if isinrange(i, j, lowx, lowy, highx, highy):
                if int(lights[i][j]) == 0:
                    lights[i][j] = 1
                else:
                    lights[i][j] = 0

def setbrightness(state, lowx, lowy, highx, highy):
    for i in range(0, lights.shape[0]):
        for j in range(0, lights.shape[1]):
            if isinrange(i, j, lowx, lowy, highx, highy):
                lights[i][j] += state
                if lights[i][j] < 0:
                    lights[i][j] = 0

# Part 1
for line in instructions:
    # print(line)  # this line was used to check progress as this program takes some time to run
    coords = re.findall(numRegex, line)
    if line[0:6] == 'toggle':
        toggle(int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
    elif line[0:8] == 'turn off':
        onoff(0, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
    elif line[0:7] == 'turn on':
        onoff(1, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))

litLights = 0
for i in range(0, lights.shape[0]):
    for j in range(0, lights.shape[1]):
        if int(lights[i][j]) == 1:
            litLights += 1

print('There are ' + str(litLights) + ' lit lights.')

# Part 2
for line in instructions:
    # print(line)  # this line was used to check progress as this program takes some time to run
    coords = re.findall(numRegex, line)
    if line[0:6] == 'toggle':
        setbrightness(2, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
    elif line[0:8] == 'turn off':
        setbrightness(-1, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
    elif line[0:7] == 'turn on':
        setbrightness(1, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))

totalBrightness = 0
for i in range(0, lights.shape[0]):
    for j in range(0, lights.shape[1]):
        totalBrightness += int(lights[i][j])

print('The brightness is ' + str(totalBrightness) + '.')




