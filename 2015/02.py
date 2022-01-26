# Day 2
import re, pyperclip # import regex and pyperclip

lwhRegex = re.compile(r'(\d+)x(\d+)x(\d+)') # setup regex to find numbers matching 123x456x789 format with any number of digits for lwh
rawDimensions = lwhRegex.findall(pyperclip.paste()) # pickup input from clipboard

paperNeeded = 0 # instantiate output variable
ribbonNeeded = 0

for i in rawDimensions: # loop through each set of lwh from the input
    l = int(i[0])  # set each dimension
    w = int(i[1])
    h = int(i[2])

    lw = l * w # set helper multiplications
    wh = w * h
    hl = h * l

    area = 2*lw + 2*wh + 2*hl + min(lw, wh, hl) #calculate area and add minimal side area

    paperNeeded += area

    ribbonLength = 2 * (l + w + h - max(l, w, h)) + (l * w * h) # add lwh and then subtract the max to get the minimum perimeter.

    ribbonNeeded += ribbonLength


print('Wrapping paper needed is ' + str(paperNeeded) + ' square feet.')
print('Ribbon  needed is ' + str(ribbonNeeded) + ' feet.')



