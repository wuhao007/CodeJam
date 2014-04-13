#!/usr/bin/python
T = int(raw_input())
i = 0
while i < T:
    cfx = [float(para) for para in raw_input().split()]
    c = cfx[0]
    f = cfx[1]
    x = cfx[2]
    i += 1
#    cookies = 0.0
#    speed = 2.0
#    farm = 0
#    while cookies < x:
#    	cookies += speed
#        if cookies >= c:
#            new_speed = speed + f
#            left = x - cookies
#            if left/speed > (left + c)/new_speed:
#                farm += 1
#                speed = new_speed
#                cookies -= c
    min_time = x/2
    for k in range(int(x/f)):
        total_time = 0.0
        speed = 2
        left = x
        for j in range(k):
            total_time += (c/speed)
            speed += f
        total_time += (left/speed)
        if total_time <= min_time:
            min_time = total_time
        else: 
            break    
    print('Case #{0}: {1:.7f}'.format(i, min_time))
