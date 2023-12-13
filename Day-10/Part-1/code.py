with open('./Day-10/input.txt', 'r') as f:
    data = f.read().split('\n')

def has_cycle_from_start(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            return True
        else:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited and graph[neighbor].count(node) == 1)
    return False

graph = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        graph[(i, j)] = []

for i in range(len(data)):
    for j in range(len(data[i])):
        char = data[i][j]
        if char == '|':
            if i >= 1:
                graph[(i, j)].append((i - 1, j)) # north
            if i < len(data) - 1:
                graph[(i, j)].append((i + 1, j)) # south
        elif char == '-':
            if j >= 1:
                graph[(i, j)].append((i, j - 1)) # west
            if j < len(data[i]) - 1:
                graph[(i, j)].append((i, j + 1)) # east
        elif char == 'L':
            if i >= 1:
                graph[(i, j)].append((i - 1, j))
            if j < len(data[i]) - 1:
                graph[(i, j)].append((i, j + 1))
        elif char == 'J':
            if i >= 1:
                graph[(i, j)].append((i - 1, j))
            if j >= 1:
                graph[(i, j)].append((i, j - 1))
        elif char == '7':
            if i < len(data) - 1:
                graph[(i, j)].append((i + 1, j))
            if j >= 1:
                graph[(i, j)].append((i, j - 1))
        elif char == 'F':
            if i < len(data) - 1:
                graph[(i, j)].append((i + 1, j))
            if j < len(data[i]) - 1:
                graph[(i, j)].append((i, j + 1)) 
        elif char == '.':
            continue
        else:
            start = (i, j)

# now find what s should be connecting
found = False
# north and south
if not found and start[0] >= 1 and start[0] < len(data) - 1:
    graph[start] = [(start[0] - 1, start[1]), (start[0] + 1, start[1])]
    if has_cycle_from_start(graph, start):
        found = True
# north and west
if not found and start[0] >= 1 and start[1] >= 1:
    graph[start] = [(start[0] - 1, start[1]), (start[0], start[1] - 1)]
    if has_cycle_from_start(graph, start):
        found = True
# north and east
if not found and start[0] >= 1 and start[1] < len(data[start[0]]) - 1:
    graph[start] = [(start[0] - 1, start[1]), (start[0], start[1] + 1)]
    if has_cycle_from_start(graph, start):
        found = True
# south and west
if not found and start[0] < len(data) - 1 and start[1] >= 1:
    graph[start] = [(start[0] + 1, start[1]), (start[0], start[1] - 1)]
    if has_cycle_from_start(graph, start):
        found = True
# south and east
if not found and start[0] < len(data) - 1 and start[1] < len(data[start[0]]) - 1:
    graph[start] = [(start[0] + 1, start[1]), (start[0], start[1] + 1)]
    if has_cycle_from_start(graph, start):
        found = True
# west and east
if not found and start[1] >= 1 and start[1] < len(data[start[0]]) - 1:
    graph[start] = [(start[0], start[1] - 1), (start[0], start[1] + 1)]
    if has_cycle_from_start(graph, start):
        found = True

# run bfs from start to count how many steps from start to each node
queue = [[start, 0]]
visited = set()
maximum = 0
while queue:
    node, steps = queue.pop(0)
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))
                if steps + 1 > maximum:
                    maximum = steps + 1

print(maximum)