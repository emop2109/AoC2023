from heapq import heappop, heappush

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()
grid = [list(map(int, [line[c] for c in range(len(line))])) for line in input]
# ---------------------------------------- Del 1 -------------------------------------------
def dijkstras(starting_position, minimum_consecutive_moves, maximum_consecutive_moves):
    seen, queue = set(), [(0, starting_position[0], starting_position[1],0,1,1)]
    while queue:
        heat, row, col, row_dir, col_dir, consecutive_moves  = heappop(queue)
        if (row, col, row_dir, col_dir, consecutive_moves) not in seen:
            seen.add((row, col, row_dir, col_dir, consecutive_moves))
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return heat
            if consecutive_moves < minimum_consecutive_moves:
                if -1 < row + row_dir < len(grid) and -1 < col + col_dir < len(grid[0]):
                    heappush(queue, (
                            heat + grid[row + row_dir][col + col_dir], row + row_dir, col + col_dir, row_dir, col_dir, consecutive_moves + 1
                        ))
            else:
                for i in range(consecutive_moves, maximum_consecutive_moves + 1):
                    for i in [-1,1]:
                        if -1 < row + i*col_dir < len(grid) and -1 < col + i*row_dir < len(grid[0]):
                            heappush(queue, (
                                heat + grid[row + i*col_dir][col + i*row_dir], row + i*col_dir, col + i*row_dir, i*col_dir, i*row_dir, 1
                            ))
                    if -1 < row + row_dir < len(grid) and -1 < col + col_dir < len(grid[0]):
                        heappush(queue, (
                            heat + grid[row + row_dir][col + col_dir], row + row_dir, col + col_dir, row_dir, col_dir, consecutive_moves + 1
                        ))
                  
print(dijkstras((0,-1), 1, 3) - grid[0][0])
# ---------------------------------------- Del 2 -------------------------------------------
print(dijkstras((0,-1), 4, 10) - grid[0][0])
