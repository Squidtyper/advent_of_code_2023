def get_color(string, color):
    n = 0
    j = 0
    pos = string.find(color)
    if (pos < 0):
        return 0
    sub = string[0:pos]
    for i in range(len(sub)-1, -1, -1):
        if sub[i].isdigit() == True:
            while sub[i].isdigit() == True:
                n = n + int(sub[i]) * pow(10, j)
                i-=1
                j+=1
            break
    return n


def get_power(string):
    draws = string.split(';')
    pow = 0
    min_blue = 0
    min_green = 0
    min_red = 0
    for i in range(len(draws)):
        blue = get_color(draws[i], "blue")
        green = get_color(draws[i], "green")
        red = get_color(draws[i], "red")
        if blue > min_blue:
            min_blue = blue
        if green > min_green:
            min_green = green
        if red > min_red:
            min_red = red
    pow = min_blue * min_green * min_red
    return pow


#the power of each game is defined by n_red * n_blue * n_green
file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
total = 0
for string in strings:
    pow = get_power(string)
    total = total + pow 
print(total)
