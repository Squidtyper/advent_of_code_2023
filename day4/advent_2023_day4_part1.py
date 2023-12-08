import math

def clean_list(l):
    while "" in l:
        l.remove("")


def checkwins(string):
    parts = string.split('|')
    n_part1 = parts[0].split(':')[1].split(' ')
    n_part2 = parts[1].split(' ')
    clean_list(n_part1)
    clean_list(n_part2)
    wins = 0
    for number in n_part2:
        if number in n_part1:
            wins += 1
    return wins
    

file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
for string in strings:
    string.strip()
total = 0
for string in strings:
    wins = checkwins(string)
    points = math.floor(2 ** (wins - 1))
    total = total + points
print (total)
