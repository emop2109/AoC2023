import re
import pandas as pd

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

hands = [tuple([c, int(b)]) for c,b in [line.split(' ') for line in input]]
card_strength = {'A': 13,'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
def merge(left, right, v2):
    results = []
    while len(left) and len(right):
        if check_winning_hand(left[0], right[0], v2):
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    while len(left):
        results.append(left.pop(0))
    while len(right):
        results.append(right.pop(0))
    return results

def merge_sort(hands, v2):
    if len(hands) == 1:
        return hands
    left, right = hands[:len(hands)//2], hands[len(hands)//2:]
    left, right = merge_sort(left, v2), merge_sort(right, v2)

    return merge(left, right, v2)

def get_maximum(card):
    c = 'J'
    if 'J' in card:
        _dict_ = {f'{x}': card.replace('J','').count(x) for x in set(card)}
        for b in [key for key in _dict_ if _dict_[key] == max(_dict_.values())]:
            c = b if card_strength[b] > card_strength[c] else c
    return card.replace('J', c)

def check_winning_hand(hand_1, hand_2, v2):
    if v2:
        left, right = set(get_maximum(hand_1[0])), set(get_maximum(hand_2[0]))
    else:
        left, right = set(hand_1[0]), set(hand_2[0])
    if len(left) == len(right):
        if v2:
            left_max, right_max = max([get_maximum(hand_1[0]).count(c) for c in left]), max([get_maximum(hand_2[0]).count(c) for c in right])
        else:
            left_max, right_max = max([hand_1[0].count(c) for c in left]), max([hand_2[0].count(c) for c in right])

        if left_max == right_max: 
            for i in range(len(hand_1[0])):
                if card_strength[hand_1[0][i]] > card_strength[hand_2[0][i]]:
                    return False
                elif card_strength[hand_1[0][i]] < card_strength[hand_2[0][i]]:
                    return True
        return False if left_max > right_max else True
    return False if len(left) < len(right) else True

# ---------------------------------------- Del 1 -------------------------------------------
sorted_hands = merge_sort(hands, False)
print(sum([(idx+1)*sorted_hands[idx][1] for idx in range(len(sorted_hands))]))
# ---------------------------------------- Del 2 -------------------------------------------
card_strength = {'A': 13,'K': 12, 'Q': 11, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
sorted_hands = merge_sort(hands, True)
print(sum([(idx+1)*sorted_hands[idx][1] for idx in range(len(sorted_hands))]))