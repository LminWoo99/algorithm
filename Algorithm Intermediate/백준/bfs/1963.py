import sys
input=sys.stdin.readline
from collections import deque
def findPrime():
    for i in range(2,100):
        if prime[i] ==True:
            for j in range(2*i, 10000, i):
                prime[j] = False
def BFS():
    dq=deque()
    dq.append((a,0))
    
    visit= [0 for i in range(10000)]
    visit[a]=1
    while dq:
        x,cnt =dq.popleft()
        strX=str(x)
        if x==b:
            return cnt
        for i in range(4):
            for j in range(10):
                temp=int(strX[:i]+str(j)+strX[i+1:])
                if visit[temp] == 0 and prime[temp] and temp>=1000:
                    visit[temp]=1
                    dq.append((temp, cnt+1))
t=int(input())
prime = [True for _ in range(10000)]
findPrime()
for i in range(t):
    a,b=map(int, input().split())
    result=BFS()
    print(result if result!= None else "Impossible")
    
