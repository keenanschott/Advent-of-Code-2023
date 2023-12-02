with open('./Advent-of-Code-2023/Day-2/input.txt', 'r') as f:
    data = f.read().split('\n')

running_sum = 0
for game in data:
    draws = game.split(':')[1].strip().split(";")
    colors = {"red" : -1, "green" : -1, "blue" : -1}
    for draw in draws:
        numbers = draw.split(',')
        for number in numbers:
            target = int(number.split()[0])
            color = number.split()[1]
            if target > colors[color]:
                colors[color] = target
    running_sum += colors["red"] * colors["green"] * colors["blue"]

print(running_sum)