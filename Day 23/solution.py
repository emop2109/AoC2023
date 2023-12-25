with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

directions = {'<': (0, -1), '>': (0, 1), 'v': (1, 0), '^': (-1, 0)}
start, end = (0, input[0].find('.')), (len(input) - 1, input[-1].find('.'))
tiles = {start: [], end: []}

def check_for_node(position):
    valid_directions = 0
    for (r, c) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not -1 < position[0] + r < len(input) or not -1 < position[1] + c < len(input[0]):
            continue
        elif input[position[0] + r][position[1] + c] == '#':
            continue
        else:
            valid_directions += 1
    return True if valid_directions > 2 else False

for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] != '#' and check_for_node((r, c)):
            tiles[(r, c)] = []

def valid_directions(position):
    valid_positions = []
    for (r, c) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not -1 < position[0] + r < len(input) or not -1 < position[1] + c < len(input[0]):
            continue
        elif input[position[0] + r][position[1] + c] == '#':
            continue
        elif input[position[0] + r][position[1] + c] == '.':
            valid_positions.append((position[0] + r, position[1] + c))
        elif (r, c) == directions[input[position[0] + r][position[1] + c]]:
            valid_positions.append((position[0] + r, position[1] + c))
    return valid_positions

def depth_first_search(position, function):
    queue, visited = [(position, 0)], []
    nodes = []
    while queue:
        (current, steps) = queue.pop()
        if current != position and current in tiles.keys():
            nodes.append((current, -steps))
        else:
            for next_position in function(current):
                if next_position not in visited:
                    queue.append((next_position, steps + 1))
        visited.append(current)
    return nodes

for tile in tiles:
    tiles[tile] = depth_first_search(tile, valid_directions)

def dijkstras(graph, start):
    queue, dist = [start], {x: 0 for x in graph}
    visited = []
    while queue:
        current_node = queue.pop(0)
        for node in graph[current_node]:
            dist[node[0]] = min(dist[node[0]], node[1] + dist[current_node])
            if node[0] not in visited:
                queue.append(node[0])
    return dist

# ---------------------------------------- Del 1 -------------------------------------------
print(-dijkstras(tiles, start)[end])
# ---------------------------------------- Del 2 -------------------------------------------
start, end = (0, input[0].find('.')), (len(input) - 1, input[-1].find('.'))
tiles = {start: [], end: []}

def valid_directions_part2(position):
    valid_positions = []
    for (r, c) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not -1 < position[0] + r < len(input) or not -1 < position[1] + c < len(input[0]):
            continue
        elif input[position[0] + r][position[1] + c] == '#':
            continue
        else:
            valid_positions.append((position[0] + r, position[1] + c))
    return valid_positions

for r in range(len(input)):
    for c in range(len(input[0])):
        if input[r][c] != '#' and check_for_node((r, c)):
            tiles[(r, c)] = []

for tile in tiles:
    tiles[tile] = depth_first_search(tile, valid_directions_part2)

def depth_first_search_part2(start, end, dist, steps, seen):
    if start == end:
        steps.append(dist)
    else:
        seen.add(start)
        for node in tiles[start]:
            if node[0] not in seen:
                depth_first_search_part2(node[0], end, node[1] + dist, steps, seen)
        seen.remove(start)

steps, seen = [], set()
depth_first_search_part2(start, end, 0, steps, seen)
print(-min(steps))