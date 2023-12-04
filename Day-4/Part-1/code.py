with open('./Day-4/input.txt', 'r') as f:
    data = f.read().split('\n')

total = 0
for card in data:
    info = card.split(':')[1]
    winning_numbers = list(map(int, [s for s in info.split('|')[0].split(' ') if s != '']))
    my_numbers = list(map(int, [s for s in info.split('|')[1].split(' ') if s != '']))
    current_total = 0
    for number in my_numbers:
        if number in winning_numbers:
            if current_total == 0:
                current_total += 1
            else:
                current_total *= 2
    total += current_total

print(total)