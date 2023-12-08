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

def find_part(parts, star):
    

def find_gears(strings, stars, parts):
    width = len(strings[0])
    height = len(strings)
    gears = []
    for star in stars:
        counter = 0
        #star[0] in x axis(character), star[1] in y axis (string)
        if star[0] > 0 and star[1] > 0:
            if strings[star[1] - 1][star[0] - 1].isdigit() == True:
                counter += 1
        if star[0] > 0:
            if strings[star[1]][star[0] - 1].isdigit() == True:
                counter += 1
        if star[0] > 0 and star[1] + 1 < width:
            if strings[star[1] + 1][star[0] - 1].isdigit() == True:
                counter += 1
        if star[1] > 0:
            if strings[star[1] - 1][star[0]].isdigit() == True:
                counter += 1
        if star[1] + 1 < height:
            if strings[star[1] + 1][star[0]].isdigit() == True:
                counter += 1
        if star[1] > 0 and star[0] + 1 < width:
            if strings[star[1] - 1][star[0] + 1].isdigit() == True:
                counter += 1
        if star[0] + 1 < width:
            if strings[star[1]][star[0] + 1].isdigit() == True:
                counter += 1
        if star[1] + 1 < height and star[0] + 1 < width:
            if strings[star[1] + 1][star[0] + 1].isdigit() == True:
                counter += 1
        print("counter value:", counter)
        if counter == 2:
            print("found star:", star)
            gears.append(star)
    return gears




#find all '*' which is adjacent to 2 numbers, return their position. 
#search their surrounding coordinates for the parts' digits's locations, if found return the parts
file = open("./testinput.txt", 'r')
content = file.read()
strings = content.split('\n')
for string in strings:
    string.strip()
parts = get_all_parts(strings)
stars = get_all_stars(strings)
#till here it is working
gears = find_gears(strings, stars)
print(gears)
pairs = find_pairs(parts, gears)
print(pairs)