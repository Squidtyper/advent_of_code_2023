def search_first_last_number(string):
    first = 0
    second = 0
    for c in string:
        if c.isdigit() == True:
            first = int(c)
            break
    for c in reversed(string):
        if c.isdigit() == True:
            second = int(c)
            break
    nbr = first * 10 + second
    print(nbr)
    return nbr


file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
total = 0
for i in range(len(strings)):
    total = total + search_first_last_number(strings[i])
print(total)