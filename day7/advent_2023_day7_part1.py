from collections import Counter
from operator import itemgetter

def clean_list(l):
    while "" in l:
        l.remove("")


def get_rank(string):
    card1, count1 = Counter(string).most_common(1)[0]
    card2, count2 = Counter(string).most_common(2)[0]
    print(card1, count1, card2, count2)
    if count1 == 5:
        return 7
    elif count1 == 4:
        return 6
    elif count1 == 3 and count2 == 2:
        return 5
    elif count1 == 3:
        return 4
    elif count1 == 2 and count2 == 2:
        return 3
    elif count1 == 2:
        return 2
    else:
        return 1

class hand:
    def __init__(self, string):
        self.cards = string.split(" ")[0]
        self.bet = int(string.split(" ")[1])
        self.rank = get_rank(self.cards)
    def __repr__(self):
        return repr((self.cards, self.bet, self.rank))
    


file = open("./testinput.txt", 'r')
content = file.read()
lines = content.split('\n')
hands = []
for line in lines:
    hands.append(hand(line))
hands.sort(reverse = True, key=lambda hand: hand.rank)
for hand in hands:
    print(hand.cards)
