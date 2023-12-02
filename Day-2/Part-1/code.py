with open('./Advent-of-Code-2023/Day-2/input.txt', 'r') as f:
    data = f.read().split('\n')

colors = {"red" : 12, "green" : 13, "blue" : 14}

id = 1
running_sum = 0
for game in data:
    draws = game.split(':')[1].strip().split(";")
    valid = True
    for draw in draws:
        numbers = draw.split(',')
        for number in numbers:
            target = int(number.split()[0])
            color = number.split()[1]
            if target > colors[color]:
                valid = False
                break
        if not valid:
            break
    if valid:
        running_sum += id
    id += 1

print(running_sum)