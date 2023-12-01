import re

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

alphabet = 'abcdefghijklmnopqrtstuvwxyz'
# ---------------------------------------- Del 1 -------------------------------------------
sum = 0
for line in input:
    n = [x for x in line if x.isdigit()]
    if len(n) > 1:
        sum += int(n[0]+n[-1])

print(sum)
# ---------------------------------------- Del 2 -------------------------------------------
numbers = {'zero': '0','one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}
sum = 0
for line in input:
    s = re.findall(f"(?=(\d|{'|'.join(numbers.keys())}))", line)
    for i in [0, -1]:
        if not s[i].isdigit():
            s[i] = numbers[s[i]]
    sum += int(s[0]+s[-1])
print(sum)
