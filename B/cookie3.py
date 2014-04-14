#!/usr/bin/python
T = int(raw_input())
i = 0
import math
while i < T:
    cfx = [float(para) for para in raw_input().split()]
    c = cfx[0]
    f = cfx[1]
    x = cfx[2]
    i += 1
    n = int(math.floor(x/c-2/f))
    total_time = 0.0
    speed = 2.0
    for j in range(n):
        total_time += c/speed
        speed += f
    total_time += x/speed
    print('Case #{0}: {1:.7f}'.format(i, total_time))
