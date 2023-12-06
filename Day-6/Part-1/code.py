with open('./Day-6/input.txt', 'r') as f:
    data = f.read().split('\n')

times = list(map(int, [x for x in data[0].split(': ')[1].split(" ") if x != '']))
distances = list(map(int, [x for x in data[1].split(': ')[1].split(" ") if x != '']))

total = 1
for i in range(len(times)):
    current_possibilities = 0
    for j in range(1, times[i]):
        if j * (times[i] - j) > distances[i]:
            current_possibilities += 1
    total *= current_possibilities

print(total)