with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()
maps = {}
i,j, pattern = 0,1, []
while i < len(input):
    if input[i] == '':
        maps[j] = pattern
        j += 1
        pattern = []
    else:
        pattern.append(input[i])
    i+=1
maps[j] = pattern

def compare_segments(pattern, left_index, right_index):
    if left_index < 0 or right_index == len(pattern):
        return True
    elif pattern[left_index] == pattern[right_index]:
        return compare_segments(pattern, left_index - 1, right_index + 1)
    else:
        return False
# ---------------------------------------- Del 1 -------------------------------------------
def get_rows(pattern, function):
    for j in range(len(pattern) - 1):
        if pattern[j] == pattern[j+1]:
            if function(pattern, j - 1, j + 2):
                return j + 1
    return 0
rows, columns = 0, 0
for key in maps:
    rows += get_rows(maps[key], compare_segments)
    columns += get_rows([''.join(row) for row in zip(*maps[key])], compare_segments)
print(rows*100+columns)

# ---------------------------------------- Del 2 -------------------------------------------
def compare_segments_version_2(pattern, left_index, right_index, checked=False):
    if left_index < 0 or right_index == len(pattern):
        return False
    elif pattern[left_index] == pattern[right_index]:
        return compare_segments_version_2(pattern, left_index - 1, right_index + 1)
    elif sum([1 if pattern[left_index][i] != pattern[right_index][i] else 0 for i in range(len(pattern[left_index]))]) == 1 and not checked:
        return not compare_segments_version_2(pattern, left_index - 1, right_index + 1, True)
    else:
        return checked
def get_rows_version_2(pattern):
    for j in range(len(pattern) - 1):
        if sum([1 if pattern[j][i] != pattern[j+1][i] else 0 for i in range(len(pattern[j]))]) == 1:
            if compare_segments(pattern, j - 1, j + 2):
                return j + 1
        elif pattern[j] == pattern[j+1]:
            if compare_segments_version_2(pattern, j - 1, j + 2):
                return j + 1
    return 0
rows, columns = 0,0
for key in maps:
    rows += get_rows_version_2(maps[key])
print(rows*100+columns)
