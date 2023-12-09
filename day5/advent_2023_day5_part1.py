import math

def clean(l):
    for i in range(len(l)):
        if l[i].isnumeric() != True:
            l.remove(l[i])
            return True
    return False

def get_ranges(string):
    lines = string.split('\n')
    content_lines = lines[1:len(lines)]
    ranges = []
    for line in content_lines:
        array = line.split(' ')
        range = []
        for item in array:
            range.append(int(item))
        ranges.append(range)
    return (ranges)
        

class almanac:
    def __init__(self, string):
        paragraph = string.split('\n\n')
        for item in paragraph:
            item.strip()
        l = paragraph[0].split(' ')
        while clean(l) == True:
            clean(l)
        self.seeds = []
        for item in l:
            self.seeds.append(int(item))
        self.s_s = get_ranges(paragraph[1])
        self.s_f = get_ranges(paragraph[2])
        self.f_w = get_ranges(paragraph[3])
        self.w_l = get_ranges(paragraph[4])
        self.l_t = get_ranges(paragraph[5])
        self.t_h = get_ranges(paragraph[6])
        self.h_l = get_ranges(paragraph[7])
        
    def seed_distance(self, s):
        for i in range(len(self.s_s)):
            if s >= self.s_s[i][1] and s < self.s_s[i][1] + self.s_s[i][2]:
                s = self.s_s[i][0] + s - self.s_s[i][1]
                break
        for i in range(len(self.s_f)):
            if s >= self.s_f[i][1] and s < self.s_f[i][1] + self.s_f[i][2]:
                s = self.s_f[i][0] + s - self.s_f[i][1]
                break
        for i in range(len(self.f_w)):
            if s >= self.f_w[i][1] and s < self.f_w[i][1] + self.f_w[i][2]:
                s = self.f_w[i][0] + s - self.f_w[i][1]
                break
        for i in range(len(self.w_l)):
            if s >= self.w_l[i][1] and s < self.w_l[i][1] + self.w_l[i][2]:
                s = self.w_l[i][0] + s - self.w_l[i][1]
                break
        for i in range(len(self.l_t)):
            if s >= self.l_t[i][1] and s < self.l_t[i][1] + self.l_t[i][2]:
                s = self.l_t[i][0] + s - self.l_t[i][1]
                break
        for i in range(len(self.t_h)):
            if s >= self.t_h[i][1] and s < self.t_h[i][1] + self.t_h[i][2]:
                s = self.t_h[i][0] + s - self.t_h[i][1]
                break
        for i in range(len(self.h_l)):
            if s >= self.h_l[i][1] and s < self.h_l[i][1] + self.h_l[i][2]:
                s = self.h_l[i][0] + s - self.h_l[i][1]
                break
        return(s)
    def s_distance(self):
        copy = self.seeds
        for i in range(len(copy)):
            copy[i] = self.seed_distance(copy[i])
        copy.sort()
        return copy[0]
            




file = open("./input.txt", 'r')
content = file.read()
alm = almanac(content)
smallest = alm.s_distance()
print(smallest)