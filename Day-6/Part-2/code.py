with open('./Day-6/input.txt', 'r') as f:
    data = f.read().split('\n')

time = int("".join(data[0].split(': ')[1].split(" ")))
distance = int("".join(data[1].split(': ')[1].split(" ")))

total = 0
for i in range(1, time):
    if i * (time - i) > distance:
        total += 1
    elif total > 0:
        break

print(total)