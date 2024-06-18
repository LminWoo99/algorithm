## 예외 사항 같은 방향의 경사로
import sys
input=sys.stdin.readline
def check(x):
    flag=True
    last=-10
    for i in range(len(x)-1):
        if x[i]!=x[i+1]:
            if x[i]<x[i+1] and abs(x[i]-x[i+1])==1:
                 if i+1>=l and len(set(x[i-(l-1):i+1]))==1 and last<=i-l:
                     last=i
                     continue
            elif x[i]>x[i+1] and abs(x[i]-x[i+1])==1:
                if i+l<n and len(set(x[i+1:i+(l+1)]))==1  and last<=i:
                     last=i+l
                     continue
            flag=False
    return flag
                     
                
n,l=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]

res=0
for i in range(n):
    tmp=set(board[i][:])
    if len(tmp)==1:
        res+=1
    else:
        if check(board[i]):
            res+=1
for tmp in zip(*board):
    tmp=list(tmp)
    if len(set(tmp))==1:
        res+=1
    else:
        if check(tmp):
            res+=1
print(res)