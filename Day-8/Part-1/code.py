with open('./Day-8/input.txt', 'r') as f:
    data = f.read().split('\n')

tree = {}
for i in range(2, len(data)):
    source, _, left, right = data[i].split()
    left, right = left[1:4], right[0:3]
    if source not in tree:
        tree[source] = []
    if left not in tree:
        tree[left] = []
    if right not in tree:
        tree[right] = []
    tree[source].append(left)
    tree[source].append(right)

steps = 0
start = 'AAA'
while True:
    current_instruction = data[0][steps % len(data[0])]
    if current_instruction == 'L':
        new_source = tree[start][0]
    else:
        new_source = tree[start][1]
    steps += 1
    if new_source == 'ZZZ':
        break
    start = new_source

print(steps)