with open('./Day-4/input.txt', 'r') as f:
    data = f.read().split('\n')

card_dict = {key + 1: 1 for key in range(len(data))}

current_card = 1
for card in data:
    info = card.split(':')[1]
    winning_numbers = list(map(int, [s for s in info.split('|')[0].split(' ') if s != '']))
    my_numbers = list(map(int, [s for s in info.split('|')[1].split(' ') if s != '']))
    current_total = 0
    for number in my_numbers:
        if number in winning_numbers:
            current_total += 1
    for _ in range(card_dict[current_card]):
        for i in range(current_card + 1, current_total + current_card + 1):
            card_dict[i] += 1
    current_card += 1

print(sum(card_dict.values()))