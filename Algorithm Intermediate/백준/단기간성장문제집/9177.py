import sys
input=sys.stdin.readline
from collections import deque
def solution(x,y, target):
    i=0
    dq=deque()
    dq.append((0,0))
    visit=[[0]*(len(y)+1) for _ in range(len(x)+1)]
    while dq:
        for _ in range(len(dq)):
            index_x, index_y=dq.popleft()
            if index_x<len(x) and visit[index_x+1][index_y]==0 and x[index_x]==target[i]:
                visit[index_x+1][index_y]=1
                dq.append((index_x+1, index_y))
            if index_y<len(y) and visit[index_x][index_y+1]==0 and y[index_y]==target[i]:
                visit[index_x][index_y+1]=1
                dq.append((index_x, index_y+1))
        i+=1
    if len(target)+1==i:
        return True
    else:
        return False
n=int(input())
for i in range(1, n+1):
    n,m,target=input().rstrip().split()
    flag=solution(n,m,target)
    if flag:
        print("Data set {}: yes".format(i))
    else:
        print("Data set {}: no".format(i))