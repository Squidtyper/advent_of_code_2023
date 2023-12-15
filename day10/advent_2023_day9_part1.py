import sys
import math

def clean_list(l):
    while "" in l:
        l.remove("")

def find_start(lines):
    height = len(lines)
    width = len(lines[0])
    for i in range(height):
        for j in range(width):
            if lines[i][j] == 'S':
                return((i, j))
    return(-1, -1)

def start(lines, start):
    j = start[1]
    i = start[0]
    height = len(lines)
    width = len(lines[0])
    count = 0
    lines[i][j] = '0'
    if j > 0:
        if lines[i][j - 1] in '-FL':
            count = move_step(lines, 1, lines[i][j - 1], (i, j - 1), height, width)
    if i > 0:
        if lines[i-1][j] in '|7F':
            count = move_step(lines, 1, lines[i - 1][j], (i - 1, j), height, width)
    if j < width - 1:
        if lines[i][j + 1] in '-J7':
            count = move_step(lines, 1, lines[i][j + 1], (i, j + 1), height, width)
    if i < height - 1:
        if lines[i + 1][j] in '|LJ':
            count = move_step(lines, 1, lines[i + 1][j], (i + 1, j), height, width)
    return count


def move_step(lines, count, pipe, point, height, width):
    i = point[0]
    j = point[1]
    lines[i][j] = '0'
    if pipe == '-':
        if j > 0 and j < width - 1:
            if lines[i][j - 1] == '0' and lines[i][j + 1] == 0:
                return count
            elif lines[i][j - 1] == '0':
                count = move_step(lines, count + 1, lines[i][j + 1], (i, j + 1), height, width)
            elif lines[i][j + 1] == '0':
                count = move_step(lines, count + 1, lines[i][j - 1], (i, j - 1), height, width)
    if pipe == '|':
        if i > 0 and i < height - 1:
            if lines[i - 1][j] == '0' and lines[i + 1][j] == '0':
                return count
            elif lines[i - 1][j] == '0':
                count = move_step(lines, count + 1, lines[i + 1][j], (i + 1, j), height, width)
            elif lines[i + 1][j] == '0':
                count = move_step(lines, count + 1, lines[i - 1][j], (i - 1, j), height, width)
    if pipe == 'L':
        if i > 0 and j < width - 1:
            if lines[i - 1][j] == '0' and lines[i][j + 1] == '0':
                return count
            elif lines[i - 1][j] == '0':
                count = move_step(lines, count + 1, lines[i][j + 1], (i, j + 1), height, width)
            elif lines[i][j + 1] == '0':
                count = move_step(lines, count + 1, lines[i - 1][j], (i - 1, j), height, width)
    if pipe == 'F':
        if i < height - 1 and j < width - 1:
            if lines[i][j + 1] == '0' and lines[i + 1][j] == '0':
                return count
            elif lines[i][j + 1] == '0':
                count = move_step(lines, count + 1, lines[i + 1][j], (i + 1, j), height, width)
            elif lines[i + 1][j] == '0':
                count = move_step(lines, count + 1, lines[i][j + 1], (i, j + 1), height, width)
    if pipe == 'J':
        if i > 0 and j > 0:
            if lines[i - 1][j] == '0' and lines[i][j - 1] == '0':
                return count
            elif lines[i - 1][j] == '0':
                count = move_step(lines, count + 1, lines[i][j - 1], (i, j - 1), height, width)
            elif lines[i][j - 1] == '0':
                count = move_step(lines, count + 1, lines[i - 1][j], (i - 1, j), height, width)
    if pipe == '7':
        if i + 1 < height and j > 0:
            if lines[i + 1][j] == '0' and lines[i][j - 1] == '0':
                return count
            elif lines[i + 1][j] == '0':
                count = move_step(lines, count + 1, lines[i][j - 1], (i, j - 1), height, width)
            elif lines[i][j - 1]  == '0':
                count = move_step(lines, count + 1, lines[i + 1][j], (i + 1, j), height, width)
    return count
    
                

sys.setrecursionlimit(100000)
file = open("./input.txt", 'r')
content = file.read()
lines = content.split('\n')
map = []
for line in lines:
    l = list(line)
    map.append(l)
startpoint = find_start(lines)
count = start(map, startpoint)
count = math.ceil(count/2)
print(count)
