import sys
input=sys.stdin.readline
import copy
from collections import deque


def solution(x,y,t):
    tmp=a[x-1]
    b=copy.deepcopy(tmp)
    if y==1:
        for i in range(len(tmp)):
            tmp[i]=b[i-1]
    elif y==-1:
        for i in range(len(tmp)-1, -1, -1):
            tmp[i-1]=b[i]
    check(x,y,t,b)
def check(x, y, t, b):
    if x+1<=4:
        if b[2]!=a[x][6] and visit[t][x+1]:
        # if a[x-1][2]!=a[x][6] and  visit[t][x+1]:
            visit[t][x+1]=0
            solution(x+1, -y,t)
    if x-1>=1:
        if b[6]!=a[x-2][2] and visit[t][x-1]:
        # if a[x-1][6]!=a[x-2][2]  and visit[t][x-1]:
            visit[t][x-1]=0
            solution(x-1, -y,t)
                    
                
        
a=[]       
for i in range(4):
    tmp=list(map(int, input().rstrip()))
    a.append((tmp))

k=int(input())
visit=[[1]*5 for _ in range(k+1)]
t=0
for i in range(k):
    x,y=map(int, input().split())
    visit[t][x]=0
    solution(x,y,t)
    t+=1
result=[]
multi=1
for i in range(1,5):
 
    if a[i-1][0]==1:
        temp=multi
    else:
        temp=0
    result.append(temp)        
    multi*=2
print(sum(result))
