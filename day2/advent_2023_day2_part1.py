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


def possible_game(string):
    draws = string.split(';')
    for i in range(len(draws)):
        blue = get_color(draws[i], "blue")
        green = get_color(draws[i], "green")
        red = get_color(draws[i], "red")
        if blue > 14 or green > 13 or red > 12:
            return False
    return True

def game_nbr(string):
    n = 0
    for i in range(len(string) -1): 
        if string[i].isdigit() == True:
            while string[i].isdigit() == True:
                n = n * 10 + int(string[i])
                i+=1
            return n
    return n

#total in bag: 12 red, 13 green, 14 blue
file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
total = 0
for i in range(len(strings)):
    if possible_game(strings[i]) == True:
        total = total + game_nbr(strings[i])
print(total)
