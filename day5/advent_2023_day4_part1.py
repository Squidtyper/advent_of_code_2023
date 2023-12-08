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
        self.s-s = get_ranges(paragraph[1])
        self.s-f = get_ranges(paragraph[2])
        self.f-w = get_ranges(paragraph[3])
        self.w-l = get_ranges(paragraph[4])
        self.l-t = get_ranges(paragraph[5])
        self.t-h = get_ranges(paragraph[6])
        self.h-l = get_ranges(paragraph[7])




file = open("./testinput.txt", 'r')
content = file.read()
alm = almanac(content)
