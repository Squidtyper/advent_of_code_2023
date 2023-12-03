def search_first_last_number(string):
    library = [("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), \
    ("6", 6), ("7", 7), ("8", 8), ("9", 9),\
    ("zero", 0), ("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), \
    ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]
    first = 0
    second = 0
    pos1 = len(string)
    for item in library:
        pos = string.find(item[0])
        if (pos >= 0):
            if pos < pos1:
                pos1 = pos
    pos2 = 0
    for item in library:
        pos = string.rfind(item[0])
        if pos > pos2:
            pos2 = pos
    for item in library:
        if (string.find(item[0], 0, pos1 + len(item[0])) != -1):
            first = item[1]
            break
    for item in library:
        if (string.find(item[0], pos2, len(string)) != -1):
            second = item[1]
            break 
    nbr = first * 10 + second
    return nbr


file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
total = 0
for i in range(len(strings)):
    total = total + search_first_last_number(strings[i])
print(total)