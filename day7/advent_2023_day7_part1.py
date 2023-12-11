from collections import Counter

def clean_list(l):
    while "" in l:
        l.remove("")


def get_type(string):
    card1, count1 = Counter(string).most_common(1)[0]
    card2, count2 = Counter(string).most_common(2)[0]
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
    return 1

class hand:
    def __init__(self, string):
        self.cards = []
        cards = string.split(" ")[0]
        for card in cards:
            if card.isdigit() == True:
                self.cards.append(int(card))
            elif card == 'A':
                self.cards.append(14)
            elif card == 'K':
                self.cards.append(13)
            elif card == 'Q':
                self.cards.append(12)
            elif card == 'J':
                self.cards.append(11)
            elif card == 'T':
                self.cards.append(10)
        self.bet = int(string.split(" ")[1])
        self.type = get_type(self.cards)
    def __repr__(self):
        return repr((self.cards, self.bet, self.type))
    


file = open("./input.txt", 'r')
content = file.read()
lines = content.split('\n')
hands = []
for line in lines:
    hands.append(hand(line))
hands.sort(key=lambda hand: (hand.type, hand.cards))
i = 0
for hand in hands:
    i+=1
    print(hand, i)
total = 0
for i in range(len(hands)):
    total = total + hands[i].bet * (i + 1)
print(total)