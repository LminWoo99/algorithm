from collections import deque
order=input()
n=int(input())
for x in range(n):
    temp=input()
    dq=deque(order)
    for j in temp:
        if j in dq:
            if j!=dq.popleft():
                print("%d  NO" %(x+1))
                break
    else:
        if len(dq)==0:
            print("%d  YES" %(x+1))        
        else:
            print("%d  NO" %(x+1))


        