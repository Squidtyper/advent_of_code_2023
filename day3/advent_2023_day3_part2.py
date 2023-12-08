def get_all_parts(strings):
    parts = []
    for i in range(len(strings)):
        j = 0
        while j < len(strings[i]):
            if strings[i][j].isdigit() == True:
                nbr = 0
                location = []
                while j < len(strings[i]) and strings[i][j].isdigit() == True:
                    nbr = nbr * 10 + int(strings[i][j])
                    coordinate = (j, i)
                    location.append(coordinate)
                    j+=1
                pair = (nbr, location)
                parts.append(pair)
            if (j < len(strings[i])):
                j+=1
    return parts

def get_all_stars(strings):
    width = len(strings[0])
    height = len(strings)
    stars = []
    for i in range(height):
        for j in range(width):
            if strings[i][j] == '*':
                stars.append((j, i))
    return stars

def find_gears(strings, stars, parts):
    gears = []
    for star in stars:
        matched = []
        points = ((star[0] - 1, star[1] - 1), (star[0] - 1, star[1]), (star[0] - 1, star[1] + 1), \
        (star[0], star[1] - 1), (star[0], star[1] + 1), \
        (star[0] + 1, star[1] - 1), (star[0] + 1, star[1]), (star[0] + 1, star[1] + 1))
        for part in parts:
            for point in points:
                if point in part[1]:
                    if part not in matched:
                        matched.append(part)
        if len(matched) == 2:
            gears.append(matched)
    return gears




#find all '*' which is adjacent to 2 numbers, return their position. 
#search their surrounding coordinates for the parts' digits's locations, if found return the parts
file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
for string in strings:
    string.strip()
parts = get_all_parts(strings)
stars = get_all_stars(strings)
gears = find_gears(strings, stars, parts)
total = 0
for gear in gears:
    power = gear[0][0] * gear[1][0]
    total = total + power
print(total)