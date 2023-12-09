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
        
def number_in_range(number, start, end):
    if number >= start and number < end:
        return True
    return False

class almanac:
    def __init__(self, string):
        paragraph = string.split('\n\n')
        for item in paragraph:
            item.strip()
        l = paragraph[0].split(' ')
        while clean(l) == True:
            clean(l)
        self.seeds = []
        for i in range(0, len(l), 2):
            self.seeds.append((int(l[i]), int(l[i]) + int(l[i + 1])))
        self.s_s = get_ranges(paragraph[1])
        self.s_f = get_ranges(paragraph[2])
        self.f_w = get_ranges(paragraph[3])
        self.w_l = get_ranges(paragraph[4])
        self.l_t = get_ranges(paragraph[5])
        self.t_h = get_ranges(paragraph[6])
        self.h_l = get_ranges(paragraph[7])
        
    def reverse_distance(self, d):
        for i in range(len(self.h_l)):
            if d >= self.h_l[i][0] and d < self.h_l[i][0] + self.h_l[i][2]:
                d = self.h_l[i][1] + d - self.h_l[i][0]
                break
        for i in range(len(self.t_h)):
            if d >= self.t_h[i][0] and d < self.t_h[i][0] + self.t_h[i][2]:
                d = self.t_h[i][1] + d - self.t_h[i][0]
                break
        for i in range(len(self.l_t)):
            if d >= self.l_t[i][0] and d < self.l_t[i][0] + self.l_t[i][2]:
                d = self.l_t[i][1] + d - self.l_t[i][0]
                break
        for i in range(len(self.w_l)):
            if d >= self.w_l[i][0] and d < self.w_l[i][0] + self.w_l[i][2]:
                d = self.w_l[i][1] + d - self.w_l[i][0]
                break
        for i in range(len(self.f_w)):
            if d >= self.f_w[i][0] and d < self.f_w[i][0] + self.f_w[i][2]:
                d = self.f_w[i][1] + d - self.f_w[i][0]
                break
        for i in range(len(self.s_f)):
            if d >= self.s_f[i][0] and d < self.s_f[i][0] + self.s_f[i][2]:
                d = self.s_f[i][1] + d - self.s_f[i][0]
                break
        for i in range(len(self.s_s)):
            if d >= self.s_s[i][0] and d < self.s_s[i][0] + self.s_s[i][2]:
                d = self.s_s[i][1] + d - self.s_s[i][0]
                break
        return(d)

    def s_distance(self):
        number = 0
        while 1:
            d = self.reverse_distance(number)
            for r in self.seeds:
                if number_in_range(d, r[0], r[1]) == True:
                    return number
            number+=1
        return number
            

#the input range is too large to test all of them
#instead test if the best result fit into the input range
file = open("./input.txt", 'r')
content = file.read()
alm = almanac(content)
smallest = alm.s_distance()
print(smallest)