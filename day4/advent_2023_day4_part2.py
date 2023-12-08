import math

class card:
    def __init__(self, string, cn):
        parts = string.split('|')
        n_part1 = parts[0].split(':')[1].split(' ')
        n_part2 = parts[1].split(' ')
        clean_list(n_part1)
        clean_list(n_part2)
        self.cn = cn
        self.part1 = n_part1
        self.part2 = n_part2

def clean_list(l):
    while "" in l:
        l.remove("")

def calculate_points(points, card, cards):
    wins = 0
    for number in card.part2:
        if number in card.part1:
            wins += 1
    points += 1
    for i in range(1, wins + 1):
        if card.cn + i >= len(cards):
            break
        points = calculate_points(points, cards[card.cn + i], cards)
    return points


#the function for calculating the number of cards should be recursive.
#if anything is won, the winning will be sent back to the same function.
file = open("./input.txt", 'r')
content = file.read()
strings = content.split('\n')
for string in strings:
    string.strip()
points = 0
cards = []
for i in range(len(strings)):
    cards.append(card(strings[i], i))
for card in cards:
    points = points + calculate_points(0, card, cards)
print(points)