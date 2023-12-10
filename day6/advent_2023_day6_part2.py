
import math

def clean_list(l):
    while "" in l:
        l.remove("")

def calc_dist(total, charge):
    dist = charge * (total - charge)
    return dist

def optimize(total, last, current, limit, count):
    if count == 20:
        print("current", current)
        return current
    if calc_dist(total, current) > limit:
        optimize(total, current, current - (abs(current - last) / 2), limit, count +1)
    else:
        optimize(total, current, current + (abs(current - last) / 2), limit, count +1)
    return current

file = open("./input.txt", 'r')
content = file.read()
lines = content.split('\n')
line1 = lines[0].split(':')
line1 = line1[1]
line1 = line1.replace(" ", "")
t = int(line1)
line2 = lines[1].split(':')
line2 = line2[1]
line2 = line2.replace(" ", "")
limit = int(line2)
charge = math.floor(optimize(t, 0, t/2, limit, 0))
print("charge", charge)
if calc_dist(t, charge) > limit:
    while calc_dist(t, charge) > limit:
        charge = math.floor(charge) - 1
else:
    while calc_dist(t, charge) < limit:
        charge = math.floor(charge) + 1
if calc_dist(t,charge) < limit:
    charge+=1
charge2 = t - charge + 1
if calc_dist(t, charge) < limit:
    charge2-=1
pos = charge2 - charge
print(pos)
