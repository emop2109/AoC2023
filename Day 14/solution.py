with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

columns = [''.join(row) for row in zip(*input)]
# ---------------------------------------- Del 1 -------------------------------------------
weight = 0
for col in columns:
    i, r = 0, []
    for index, object in enumerate(col):
        if object == 'O':
            r.append(len(col) - i)
            i += 1
        elif object == '#':
            i = index + 1
    weight += sum(r)
print(weight)

# ---------------------------------------- Del 2 -------------------------------------------
def tilt(map, dir='n'):
    tilts = {'n': (0, len(map), 1, len(map[0]), len(map), 0),
             'e': (len(map[0]) - 1, -1, -1, len(map), len(map[0]), len(map[0]) - 1),
             's': (len(map) - 1, -1, -1, len(map[0]), len(map), len(map) - 1),
             'w': (0, len(map[0]), 1, len(map), len(map[0]), 0)}
    start_index, stop_index, iterator, q, v, n = tilts[dir]
    if dir in 'ns':
        for c in range(q):
            j, rocks = n,[]
            for r in range(start_index, stop_index, iterator):
                if map[r][c] == 'O':
                    rocks.append(j)
                    j = j + 1 if dir == 'n' else j - 1
                elif map[r][c] == '#':
                    j = r + 1 if dir == 'n' else r - 1
            for r in range(v):
                if r in rocks:
                    map[r][c] = 'O'
                elif map[r][c] != '#':
                    map[r][c] = '.'
    else:
        for r in range(q):
            j,rocks = n,[]
            for c in range(start_index, stop_index, iterator):
                if map[r][c] == 'O':
                    rocks.append(j)
                    j = j + 1 if dir == 'w' else j - 1
                elif map[r][c] == '#':
                    j = c + 1 if dir == 'w' else c - 1
            for c in range(v):
                if c in rocks:
                    map[r][c] = 'O'
                elif map[r][c] != '#':
                    map[r][c] = '.'

def calculate_weight(map):
    weight = 0
    for r in range(len(map)):
        weight += sum([1 if map[r][c] == 'O' else 0 for c in range(len(map[0]))])*(len(map)-(r))
    return weight

def simulate_steps(n):
    weights = []
    for i in range(n):
        tilt(map)
        tilt(map, 'w')
        tilt(map, 's')
        tilt(map, 'e')
        weights.append(calculate_weight(map))
        if i%1000 == 0:
            tortoise, hare = 0,1
            while hare < len(weights):
                if weights[tortoise] == weights[hare]:
                    return weights[tortoise+((n-tortoise)%(hare-tortoise))-1]
                tortoise += 1
                hare += 2
        weights = [] if len(weights) > 10_000 else weights
map = [[c for c in r] for r in input]

print(simulate_steps(1000000000))