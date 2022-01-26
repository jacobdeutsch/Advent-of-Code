# Day 10

# I just needed to make a not to never run this again.  Took about 3 days to run 50 and about 8 hours to run 40 iterations.
import re

puzzleInput = '1321131112'
#firstAnswer = '11131221133112'  for reference while debugging




def lookandsay(input):
    result = ''
    for i in range(1, len(input)):     # look at digit before and compare to current.  if different run regex to get count. if same move to next.  special case for last digit try except?
        #print('On digit %d of %d.' % (i, len(input)))
        if input[i] != input[i - 1]:        # if digits not equal, run regex on substring up to but excluding current digit.
            regex = re.compile(r'[' + input[i - 1] + ']+$')     # regex that finds how many of the previous digit there are
            #result += str(len(re.findall(regex, input[0:i])[0]))
            #result += input[i - 1]
            result = ''.join([result, str(len(re.findall(regex, input[0:i])[0])), input[i - 1]])

        if i == len(input) - 1:
            regex = re.compile(r'[' + input[i] + ']+$')  # regex that finds how many of the previous digit there are
            result += str(len(re.findall(regex, input)[0]))
            result += input[i]

    return result

for i in range(0, 50):  # run 50 times
    print('Running iteration %d.' % i)
    puzzleInput = lookandsay(puzzleInput)

print('The length of the result is %d.' % len(puzzleInput))
