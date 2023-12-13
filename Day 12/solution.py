from functools import cache

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

@cache
def calculate_combinations(remaining_string, digits, results=0):
    if len(digits) == 0:
        return 1 if '#' not in remaining_string else 0
    current_digit, digits = digits[0], digits[1:]
    for j in range(len(remaining_string) - len(digits) - sum(digits) - current_digit + 1):
        if '#' in remaining_string[:j]:
            break
        if j+current_digit <= len(remaining_string) and '.' not in remaining_string[j:j+current_digit] and remaining_string[j+current_digit:j+current_digit+1] != '#':
            results += calculate_combinations(remaining_string[j+current_digit + 1:], digits)
    return results

# ---------------------------------------- Del 1 -------------------------------------------
print(sum([calculate_combinations(line.split()[0], tuple(map(int, line.split()[1].split(',')))) for line in input]))
# ---------------------------------------- Del 2 -------------------------------------------
print(sum([calculate_combinations('?'.join([line.split()[0]]*5), tuple(map(int, line.split()[1].split(',')))*5) for line in input]))