from functools import cache

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

@cache
def calculate_next_position(row, column, row_dir, col_dir, character):
    match character:
        case '\\':
            return [(row + col_dir, column + row_dir, col_dir, row_dir)]
        case '/':
            return [(row - col_dir, column - row_dir, -col_dir, -row_dir)]
        case '|':
            return [(row + col_dir, column, col_dir, 0), 
                    (row - col_dir, column, -col_dir, 0)
                    if col_dir != 0 else (row + row_dir, column, row_dir, col_dir)]
        case '-':
            return [(row, column + row_dir, 0, row_dir), 
                    (row, column - row_dir, 0, -row_dir) 
                    if row_dir != 0 else (row, column + col_dir, row_dir, col_dir)]
        case '.':
            return [(row + row_dir, column + col_dir, row_dir, col_dir)]
          
def depth_first_search(starting_position):
    visited, queue = set(), [starting_position]
    while len(queue):
        (row, column, row_dir, col_dir) = queue.pop()
        if (row, column, row_dir, col_dir) not in visited and -1 < row < len(input) and -1 < column < len(input[0]):
            queue.extend(calculate_next_position(row, column, row_dir, col_dir, input[row][column]))
            visited.add((row, column, row_dir, col_dir))
    return len(set((x,y) for x, y, row_dir, col_dir in visited))
# ---------------------------------------- Del 1 -------------------------------------------
print(depth_first_search((0,0,0,1)))
# ---------------------------------------- Del 2 -------------------------------------------
vertical = max([depth_first_search((len(input)*n, c, (-1)**n,0)) for n in [0, 1] for c in range(len(input[0]))])
horizontal = max([depth_first_search((r, len(input[0])*n,0,(-1)**n)) for n in [0, 1] for r in range(len(input))])
print(max(vertical, horizontal))