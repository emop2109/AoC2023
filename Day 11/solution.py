with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

def get_universe(input):
    rows = [0]
    for i in range(1, len(input)):
        if '#' in input[i]:
            rows.append(rows[-1])
        else:
            rows.append(rows[-1] + 1)
    transposed_universe = [''.join(r) for r in zip(*input)]
    columns = [0]
    for i in range(1, len(transposed_universe)):
        if '#' in transposed_universe[i]:
            columns.append(columns[-1])
        else:
            columns.append(columns[-1] + 1)
    return rows, columns

def get_paths(n):
    row,col = get_universe(input)
    galaxies = {(r + row[r]*n,c + col[c]*n): [] for r in range(len(input)) for c in range(len(input[0])) if input[r][c] == '#'}
    visited = []
    for key in galaxies:
        visited.append(key)
        for k in galaxies:
            if k not in visited:
                galaxies[key].append(abs(key[0]-k[0]) + abs(key[1]-k[1]))
    return sum([sum(d) for d in galaxies.values()])
# ---------------------------------------- Del 1 -------------------------------------------
print(get_paths(1))
# ---------------------------------------- Del 2 -------------------------------------------
print(get_paths(1_000_000-1))
