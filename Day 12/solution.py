import re

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

def valid_character(string, remaining_string, next_character, sequence):
    occurences = re.findall(r'#+', string+next_character)
    if len(occurences):
        if len(occurences) > len(sequence):
            return False
        elif any(len(occurences[i]) != sequence[i] for i in range(len(occurences) - 1)):
            return False
        elif len(occurences[-1]) > sequence[len(occurences) - 1]:
            return False
        elif sum(sequence) - sum([len(x) for x in occurences]) > len(remaining_string):
            return False
    return True
def generate_string(remaining_string, current_string, sequence):
    if len(remaining_string) == 0:
        occurences = re.findall(r'#+', current_string)
        return 1 if len(occurences) == len(sequence) and all([len(occurences[i]) == sequence[i] for i in range(len(occurences))]) else 0
    elif remaining_string[0] != '?':
        return generate_string(remaining_string[1:], current_string+remaining_string[0], sequence)
    else:
        return sum([generate_string(remaining_string[1:], current_string+q, sequence) if valid_character(current_string, remaining_string[1:], q, sequence) else 0 for q in ['#', '.']])

# ---------------------------------------- Del 1 -------------------------------------------
_sum_ = 0
for line in input:
    d = [int(x) for x in re.findall(r'\d+', line)]
    _sum_ += generate_string(line.split(' ')[0], '', d)
print(_sum_)

# ---------------------------------------- Del 2 -------------------------------------------
_sum_, _ = 0,0
for line in input:
    d = [int(x) for x in re.findall(r'\d+', line)]
    string = line.split(' ')[0] + '?' + line.split(' ')[0] + '?' + line.split(' ')[0] + '?' + line.split(' ')[0] + '?' + line.split(' ')[0]
    _ = generate_string(string, '', [x for i in [0,1,2,3,4] for x in d])
    print(string, _)
    _sum_ += _
print(_sum_)
