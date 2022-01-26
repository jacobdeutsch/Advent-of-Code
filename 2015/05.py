# Day 5

import re, pyperclip

strings = pyperclip.paste().splitlines()

# Part 1
vowelRegex = re.compile(r'[aeiou]{1}')  # needs to match 3 or more of these
repeatRegex = re.compile(r'(\w)\1+')  # needs to match 1 or more of these
naughtyRegex = re.compile(r'ab|cd|pq|xy')  # needs to match none of these

niceStrings = 0

for i in strings:
    if len(re.findall(vowelRegex, i)) >= 3:
        if len(re.findall(repeatRegex, i)) >= 1:
            if len(re.findall(naughtyRegex, i)) == 0:
                niceStrings += 1

print('There are ' + str(niceStrings) + ' nice strings.')

# Part 2
repeatRegex = re.compile(r'(\w\w)\w*\1')  # needs to match 1 or more of these
repeatRegex2 = re.compile(r'(\w)\w\1+')  # needs to match 1 or more of these

niceStrings = 0

for i in strings:
    if len(re.findall(repeatRegex, i)) >= 1:
        if len(re.findall(repeatRegex2, i)) >= 1:
            niceStrings += 1

print('There are now ' + str(niceStrings) + ' nice strings.')
