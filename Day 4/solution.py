with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

def winning_numbers(card):
    return len(
        set([int(x) for x in card.split(' |')[0].split(': ')[1].split(' ') if x.isdigit()]).intersection(
            set([int(x) for x in card.split('| ')[1].split(' ') if x.isdigit()])
        )
    )
# ---------------------------------------- Del 1 -------------------------------------------
_sum_ = 0
for card in input:
    n = winning_numbers(card)
    _sum_ += 2**(n-1) if n != 0 else 0
print(_sum_)
# ---------------------------------------- Del 2 -------------------------------------------
cards = {(idx + 1) : 1 for idx in range(0,len(input))}
for idx, card in enumerate(cards.keys()):
    for i in range(idx+2, idx+2+winning_numbers(input[idx])):
        cards[i] += cards[idx+1]
print(sum(cards.values()))