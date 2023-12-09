with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

def get_values(i):
    values = []
    for line in input:
        sequence = [[int(x) for x in line.split()]]
        while sum(sequence[-1]) != 0:
            sequence.append([sequence[-1][n] - sequence[-1][n-1] for n in range(1, len(sequence[-1]))])
        sequence[-1].append(0)
        for n in range(len(sequence) - 1, 0, -1):
            if i == -1:
                sequence[n-1].append(sequence[n-1][-1] + sequence[n][-1])
            else:
                sequence[n-1].insert(0, sequence[n-1][0] - sequence[n][0])
        values.append(sequence[0][i])
    return sum(values)
# ---------------------------------------- Del 1 -------------------------------------------
print(get_values(-1))
# ---------------------------------------- Del 2 -------------------------------------------
print(get_values(0))