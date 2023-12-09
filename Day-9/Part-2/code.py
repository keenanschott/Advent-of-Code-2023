with open('./Day-9/input.txt', 'r') as f:
    data = f.read().split('\n')

total = 0
for line in data:
    histories = [list(map(int, line.split(' ')))]
    while True:
        history = []
        for i in range(len(histories[-1]) - 1):
            history.append(histories[-1][i + 1] - histories[-1][i])
        histories.append(history)
        if any(element != 0 for element in history):
            continue
        break
    histories = histories[::-1]
    for i in range(1, len(histories)):
        histories[i].insert(0, histories[i][0] - histories[i - 1][0])
    total += histories[-1][0]

print(total)