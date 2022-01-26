# Day 8
import re, pyperclip

instructions = pyperclip.paste().splitlines()  # read input into split line list

stringCharacters = 0    # number of characters in the line including beginning and ending ""
memoryCharacters = 0    # number of characters stored in memory (or would be printed if properly parsed)
longStringCharacters = 0    # for part 2

slashEscapeRegex = re.compile(r'(\\\\){1}')
quoteEscapeRegex = re.compile(r'(\\\"){1}')      # find anything with \\ or \"
asciiRegex = re.compile(r'\\x[0-9a-f]{2}')  # find anything with \x followed by 2 hex digits


for line in instructions:
    memoryLength = len(line)
    longLength = len(line)
    stringCharacters += memoryLength

    memoryLength -= 2       # remove 2 for the beginning and end quotes
    longLength += 4         # add 4 for start and end quotes

    numSlash = re.findall(slashEscapeRegex, line[1:len(line) - 1])
    numQuote = re.findall(quoteEscapeRegex, line[1:len(line) - 1])
    numAscii = re.findall(asciiRegex, line[1:len(line) - 1])

    memoryLength -= len(numSlash)
    memoryLength -= len(numQuote)
    memoryLength -= 3 * len(numAscii)

    longLength += 2 * len(numSlash)
    longLength += 2 * len(numQuote)
    longLength += len(numAscii)

    memoryCharacters += memoryLength
    longStringCharacters += longLength

print('Number of string characters: %d.\nNumber of memory characters: %d.\nString minus memory: %d.\nLong strings minus string: %d.' % (stringCharacters, memoryCharacters, (stringCharacters - memoryCharacters), (longStringCharacters - stringCharacters)))
