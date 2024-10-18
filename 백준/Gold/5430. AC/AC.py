import sys
input=sys.stdin.readline
from collections import deque
    
t=int(input())
for _ in range(t):
    p=input().rstrip() # 수행할 함수
    n=int(input()) # 배열에 들어있는 정수
    a=input().rstrip()
    a=deque(a[1:-1].split(','))
    cnt=0 # rotate를 할지말지
    flag=False
    for command in p:
        if command=='D':
            if n<=0:
                flag=True
                break
            else:
                if cnt%2==0:
                    a.popleft()
                else:
                    a.pop()
            n-=1
        else:
            cnt+=1
    if cnt%2==1:
        a.reverse()
    if flag:
        print("error")
    else:
        print('['+','.join(a)+']')
