import math

def examine_rules(seed, rules):
    for rule in rules:
        if rule[1] <= seed <= rule[2]:
            return rule[0] + seed - rule[1]
    return seed

def create_rules(data, start):
    rules = []
    start += 2
    while True:
        if start == len(data) or data[start] == '':
            break
        destination, source, range_ = list(map(int, (data[start].split(' '))))
        rules.append((destination, source, source + range_ - 1))
        start += 1
    return start, rules

with open('./Day-5/input.txt', 'r') as f:
    data = f.read().split('\n')

seeds = list(map(int, data[0].split(': ')[1].split(' ')))

all_rules = []
start = 1
for _ in range(7):
    start, rules = create_rules(data, start)
    all_rules.append(rules)

# If you're reading this comment, it means I brute-forced the answer using 
# what was pretty much my answer from Part-1 and have yet to come up with 
# something clever. Hopefully, you're not reading this comment!
min = math.inf
for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
        for rules in all_rules:
            seed = examine_rules(seed, rules)
        if seed < min:
            min = seed
        
print(min)