import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
def DFS(start):
    global res
    visit[start]=1
    tmp.append(start)
    student=a[start]
    if visit[student]==1:
        if student in tmp:
            res+=tmp[tmp.index(student):]
        return            
    else:
        DFS(a[start])

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))   
    a=[0]+a
    res=[]
    visit=[0]*(n+1)
    for i in range(1, n+1):
        if not visit[i]:
            tmp=[]
            DFS(i)
    print(n-len(res))