import re

with open('.\input.txt', 'r') as file:
    input=file.read().split(',')
# ---------------------------------------- Del 1 -------------------------------------------
_sum_ = []
for line in input:
    current_value = 0
    for c in line:
        current_value = ((current_value+ord(c))*17)%256
    _sum_.append(current_value)
print(sum(_sum_))
# ---------------------------------------- Del 2 -------------------------------------------
def get_index(labels, label):
    for idx, lab in enumerate(labels):
        if label == lab.split()[0]:
            return idx


boxes = {i : [] for i in range(256)}
for line in input:
    current_box = 0
    for c in re.findall(r'[a-zA-z]', line):
        current_box = ((current_box+ord(c))*17)%256
    if '=' in line:
        try:
            boxes[current_box][get_index(boxes[current_box], line.split('=')[0])] = line.replace('=', ' ')
        except TypeError:
            boxes[current_box].append(line.replace('=', ' '))
    else:
        try:
            boxes[current_box].pop(get_index(boxes[current_box], line[:-1]))
        except TypeError:
            continue

_sum_ = 0
for key in boxes:
    for idx, values in enumerate(boxes[key]):
        _sum_ += (key+1)*(idx+1)*int(values[-1])
print(_sum_)