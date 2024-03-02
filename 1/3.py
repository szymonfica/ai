import random

suits = ['clubs', 'diamonds', 'hearts', 'spades']
faces  = ['J', 'Q', 'K', 'A']
numbers  = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
deck_F = [(v, s) for s in suits for v in faces]
deck_B = [(v, s) for s in suits for v in numbers]
#deck_B = [(v, s) for v in ['8', '9', '10'] for s in suits]

'''
0 - high card
1 - pair
2 - two pairs
3 - three of a kind
4 - straight
5 - flush
6 - full house
7 - four of a kind
8 - straight flush
9 - royal flush
'''

def eval(hand):
    hand.sort()

    if hand[0][0] in numbers and int(hand[0][0])+1 == int(hand[1][0]) and int(hand[1][0])+1 == int(hand[2][0]) and int(hand[2][0])+1 == int(hand[3][0]) and int(hand[3][0])+1 == int(hand[4][0]) and hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        return 8

    for i in range(2):
        if hand[i][0] == hand[i+1][0] and hand[i+1][0] == hand[i+2][0] and hand[i+2][0] == hand[i+3][0]:
            return 7
        
    if (hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]) or (hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]):
        return 6
                   
    if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]:
        return 5
    
    if hand[0][0] in numbers and int(hand[0][0])+1 == int(hand[1][0]) and int(hand[1][0])+1 == int(hand[2][0]) and int(hand[2][0])+1 == int(hand[3][0]) and int(hand[3][0])+1 == int(hand[4][0]):
        return 4

    for i in range(3):
        if hand[i][0] == hand[i+1][0] and hand[i+1][0] == hand[i+2][0]:
            return 3
            
    for i in range(2):
        for j in range(i+2, 4):
            if hand[i][0] == hand[i+1][0] and hand[j][0] == hand[j+1][0]:
                return 2

    for i in range(4):
            if hand[i][0] == hand[i+1][0]:
                return 1
    return 0

def game():
    random.seed()
    hand_F, hand_B = [], []
    hand_F = random.sample(deck_F, 5)
    hand_B = random.sample(deck_B, 5)

    #print(f"{eval(hand_F)} = {hand_F}")
    #print(f"{eval(hand_B)} = {hand_B}")

    return eval(hand_F) < eval(hand_B)

rounds, score = 1000, 0
for _ in range(rounds):
    if game():
        score += 1

print(f"score: {score} : {rounds-score}")
print(f"win rate: {100*score/rounds}%")