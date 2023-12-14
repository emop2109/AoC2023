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
def compare_segments_version_2(pattern, left_index, right_index):
    if left_index < 0 or right_index == len(pattern):
        return False
    elif pattern[left_index] == pattern[right_index]:
        return compare_segments_version_2(pattern, left_index - 1, right_index + 1)
    elif abs(pattern[left_index].count('#') - pattern[right_index].count('#')) == 1:
        return not compare_segments_version_2(pattern, left_index - 1, right_index + 1)
    else:
        return False
rows, columns = 0,0
for key in maps:
    rows += get_rows(maps[key], compare_segments_version_2)
    columns += get_rows([''.join(row) for row in zip(*maps[key])], compare_segments_version_2)
print(rows*100+columns)
