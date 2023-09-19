import sys
input=sys.stdin.readline
def DFS(L, idx):
    if L==n:
        return
    for i in range(idx, len(s)):
        res.append(s[i])
        check[sum(res)-1]=1
        DFS(L+1, i+1)
        res.pop()
check=[0]*2000000
n=int(input())
s=list(map(int, input().split()))
res=[]
DFS(0,0)
j=0
while True:
    if check[j]==0:
        print(j+1)
        break
    j+=1
