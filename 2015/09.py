# Day 9
import re, pyperclip, random, math

instructions = pyperclip.paste().splitlines()  # read input into split line list
cityPair = {}       # empty library to store city pairs as keys with distance as value
cityList = []       # empty dictionary to store cities
shortestRouteLength = 999999999999           # long number so first guess will always be less than
longestRouteLength = 0

cityRegex = re.compile(r'(\w+)\sto\s(\w+)')     # pulls both cities (single words separated by " to ")
distanceRegex = re.compile(r'\d+$')             # gets the distance

for line in instructions:
    cityOne = re.findall(cityRegex, line)[0][0]
    cityTwo = re.findall(cityRegex, line)[0][1]
    distance = int(re.findall(distanceRegex, line)[0])

    cityPair[cityOne + cityTwo] = distance      # store citypairs as AB and BA
    cityPair[cityTwo + cityOne] = distance

    if cityOne not in cityList:
        cityList.append(cityOne)
    if cityTwo not in cityList:
        cityList.append(cityTwo)

# Generate routes
# I can't figure out a way to quickly generate routes, so I'm going to randomly shuffle them.  Total
# options is routes! (Routes factorial) so to ensure this works, I'm going to do (routes + 1)!

for i in range(0, math.factorial(len(cityList))):
    random.shuffle(cityList)        # this function shuffes cityList, so you can't do an x = random.shuffle(list).

    routeLength = 0
    # calculate distance
    for j in range(0, len(cityList) - 1):
        routeLength += cityPair[cityList[j] + cityList[j + 1]]

    if routeLength < shortestRouteLength:
        shortestRouteLength = routeLength

    if routeLength > longestRouteLength:
        longestRouteLength = routeLength

print('The shortest route length is %d miles long.\nThe longest route is %d miles long.' % (shortestRouteLength, longestRouteLength))
