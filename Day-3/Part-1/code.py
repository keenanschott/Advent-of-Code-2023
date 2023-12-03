with open('./Day-3/input.txt', 'r') as f:
    data = f.read().split('\n')

def adjacent(data, i, j):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue 
            new_i, new_j = i + x, j + y
            if 0 <= new_i < len(data) and 0 <= new_j < len(data[i]):
                if (not data[new_i][new_j].isdigit()) and data[new_i][new_j] != '.':
                    return True
    return False

sum_parts = 0
for i in range(len(data)):
    current_number = ''
    add = False
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            current_number += data[i][j]
            if not add and adjacent(data, i, j):
                add = True
        else:
            if current_number != '' and add:
                sum_parts += int(current_number)
            add = False
            current_number = ''
        if j == len(data[i]) - 1 and current_number != '' and add:
            sum_parts += int(current_number)

print(sum_parts)