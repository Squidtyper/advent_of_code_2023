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

def is_special_character(c):
    if c.isdigit() != True and c != '\0' and c != '.':
        return True
    return False

def if_adjacent(strings, part):
    width = len(strings[0])
    height = len(strings)
    for digit in part[1]:
        #digit[0] in x axis(character), digit[1] in y axis (string)
            if digit[0] > 0 and digit[1] > 0:
                if is_special_character(strings[digit[1] - 1][digit[0] - 1]) == True:
                    return True
            if digit[0] > 0:
                if is_special_character(strings[digit[1]][digit[0] - 1]) == True:
                    return True
            if digit[0] > 0 and digit[1] + 1 < width:
                if is_special_character(strings[digit[1] + 1][digit[0] - 1]) == True:
                    return True
            if digit[1] > 0:
                if is_special_character(strings[digit[1] - 1][digit[0]]) == True:
                    return True
            if digit[1] + 1 < height:
                if is_special_character(strings[digit[1] + 1][digit[0]]) == True:
                    return True
            if digit[1] > 0 and digit[0] + 1 < width:
                if is_special_character(strings[digit[1] - 1][digit[0] + 1]) == True:
                    return True
            if digit[0] + 1 < width:
                if is_special_character(strings[digit[1]][digit[0] + 1]) == True:
                    return True
            if digit[1] + 1 < height and digit[0] + 1 < width:
                if is_special_character(strings[digit[1] + 1][digit[0] + 1]) == True:
                    return True
    return False




#store digits' numbers and their positions in a pair
#check the surroundings of the positions for a special character
file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
for string in strings:
    string.strip()
parts = get_all_parts(strings)
confirmed = []
for part in parts:
    if if_adjacent(strings, part) == True:
        confirmed.append(part[0])
total = sum(confirmed)
print(total)