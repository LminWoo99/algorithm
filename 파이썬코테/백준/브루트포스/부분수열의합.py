import sys
input=sys.stdin.readline
def DFS(L, idx):
    global cnt
    if L==s:
        cnt+=1
    for i in range(idx, n):
        L+=a[i]        
        DFS(L, i+1)
        L-=a[i]

n,s=map(int, input().split())
a=list(map(int, input().split()))
cnt=0
DFS(0,0)
if s==0:
    cnt-=1
print(cnt)