#!/usr/bin/python

import sys
fout = open('result.txt', 'a')
T = int(raw_input())
s = 0
while s < T:
    cfx = [int(para) for para in raw_input().split()]
    r = cfx[0]
    c = cfx[1]
    m = cfx[2]
    s += 1

    if r > 1 and c > 1: 
        if (r*c - m) > 3:
            fout.write('Case #' + str(s) + ':\n')
        else:   
            fout.write('Case #' + str(s) + ':\nImpossible\n')
            continue
    elif r == 1 or c == 1:
        if (r*c - m) > 1:
            fout.write('Case #' + str(s) + ':\n')
        else:   
            fout.write('Case #' + str(s) + ':\nImpossible\n')
            continue

    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            if ((i == (r - 2) and j == (c - 1)) or (i == (r - 1) and j == (c - 2)) or (i == (r - 2) and j == (c - 2))):
                row += ['.']
            elif (i == (r - 1) and j == (c - 1)):
                row += ['c']
            elif m > 0:
                row += ['*']
                m -= 1
            else:
                row += ['.']
        matrix += [row]         

    for i in range(r):
        for j in range(c):
            fout.write(matrix[i][j])
        fout.write('\n')
fout.close()
