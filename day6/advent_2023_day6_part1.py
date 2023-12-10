
def clean_list(l):
    while "" in l:
        l.remove("")

def possible_solutions(number, limit):
    sol = 0
    for charge in range(1, number - 1, 1):
        dist = (number - charge) *charge
        if dist > limit:
            sol+=1
    return sol


file = open("./input.txt", 'r')
content = file.read()
lines = content.split('\n')

line1 = lines[0].split(' ')
clean_list(line1)
line1 = line1[1:len(line1)]
t= []
for item in line1:
    t.append(int(item))
line2 = lines[1].split(' ')
clean_list(line2)
line2 = line2[1:len(line2)]
dist = []
for item in line2:
    dist.append(int(item))
pos = []
for i in range(len(t)):
    pos.append(possible_solutions(t[i], dist[i]))
sol = pos[0]*pos[1]*pos[2]*pos[3]
print(sol)