with open('./Day-3/input.txt', 'r') as f:
    data = f.read().split('\n')

def adjacent(data, i, j):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue 
            new_i, new_j = i + x, j + y
            if 0 <= new_i < len(data) and 0 <= new_j < len(data[i]):
                if data[new_i][new_j] == '*':
                    return (new_i, new_j)
    return False

gear_grid = [[[] for _ in range(len(data))] for _ in range(len(data))]
for i in range(len(data)):
    current_number = ''
    add = False
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            current_number += data[i][j]
            if not add:
                add = adjacent(data, i, j)
            if add and (j == len(data[i]) - 1 or not data[i][j + 1].isdigit()):
                gear_grid[add[0]][add[1]].append(int(current_number))
        else:
            add = False
            current_number = ''

total = 0
for i in range(len(gear_grid)):
    for j in range(len(gear_grid[i])):
        if len(gear_grid[i][j]) == 2:
            total += gear_grid[i][j][0] * gear_grid[i][j][1]

print(total)