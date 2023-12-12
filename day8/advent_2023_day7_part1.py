from collections import Counter

class map_element:
    def __init__(self, string):
        parts = string.split('=')
        self.mark = parts[0].strip()
        self.instructions = parts[1].split(',')
        self.instructions[0] = self.instructions[0].strip().replace('(', '')
        self.instructions[1] = self.instructions[1].strip().replace(')', '')
    def __repr__(self):
        return repr((self.mark, self.instructions))
    
def move_to(map, string):
    for element in map:
        if element.mark == string:
            return element
    

file = open("./input.txt", 'r')
content = file.read()
lines = content.split('\n')
map = []
for line in lines[2:len(lines)]:
    map.append(map_element(line))
route = lines[0]
location = move_to(map, 'AAA')
counter = 0
i = 0
while (1):
    if i == len(route):
        i = 0
    if route[i] == 'L':
        location = move_to(map, location.instructions[0])
    elif route[i] == 'R':
        location = move_to(map, location.instructions[1])
    counter+=1
    i+=1
    if location.mark == 'ZZZ':
        break
print(counter)
