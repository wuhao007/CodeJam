#!/usr/bin/python
T = int(raw_input())
i = 0
while i < T:
    base = 10*i
    first_ans = int(raw_input())
    lines = [raw_input() for j in range(4)]
    first_cards = set([int(card) for card in lines[first_ans - 1].split()])
    second_ans = int(raw_input())
    lines = [raw_input() for j in range(4)]
    second_cards = set([int(card) for card in lines[second_ans - 1].split()])
    card = first_cards.intersection(second_cards) 
    i += 1
    n = len(card)
    if n == 0:
        print 'Case #' + str(i) + ': Volunteer cheated!'
    elif n == 1:
        print 'Case #' + str(i) + ': ' + str(card.pop())  
    elif n > 1:
        print 'Case #' + str(i) + ': Bad magician!'
