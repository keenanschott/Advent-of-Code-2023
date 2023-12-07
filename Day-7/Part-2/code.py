with open('./Day-7/input.txt', 'r') as f:
    data = f.read().split('\n')

def my_sort(element):
    return ["J23456789TQKA".index(char) for char in element[0]]

def adjust_for_joker(all_cards):
    if 'J' in all_cards.keys():
        max_key = max(all_cards, key=all_cards.get)
        edge_case = 0
        if max_key == 'J':
            edge_case = all_cards[max_key]
            del all_cards[max_key]
            max_key = max(all_cards, key=all_cards.get)
        if edge_case == 0:
            all_cards[max_key] += all_cards['J']
            del all_cards['J']
        else:
            all_cards[max_key] += edge_case
    return all_cards

all_hands = [[] for _ in range(7)]

for line in data:
    hand, bid = line.split(' ')
    all_cards = {}
    for card in hand:
        if card in all_cards:
            all_cards[card] += 1
        else:
            all_cards[card] = 1
    if len(all_cards) == 1 or (len(all_cards) == 2 and 'J' in all_cards.keys()):
        all_hands[0].append((hand, bid))
    elif len(all_cards) == 2 or (len(all_cards) == 3 and 'J' in all_cards.keys()):
        all_cards = adjust_for_joker(all_cards)
        if 4 in all_cards.values():
            all_hands[1].append((hand, bid))
        else:
            all_hands[2].append((hand, bid))
    elif len(all_cards) == 3 or (len(all_cards) == 4 and 'J' in all_cards.keys()):
        all_cards = adjust_for_joker(all_cards)
        if 3 in all_cards.values():
            all_hands[3].append((hand, bid))
        else:
            all_hands[4].append((hand, bid))
    elif len(all_cards) == 4 or (len(all_cards) == 5 and 'J' in all_cards.keys()):
        all_hands[5].append((hand, bid))
    else:
        all_hands[6].append((hand, bid))

for i in range(7):
    all_hands[i] = sorted(all_hands[i], key=my_sort)

total = 0
current_multiplier = 1
for i in range(7, 0, -1):
    for hand in all_hands[i - 1]:
        total += int(hand[1]) * current_multiplier
        current_multiplier += 1

print(total)