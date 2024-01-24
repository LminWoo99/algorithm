import sys
input=sys.stdin.readline
sys.setrecursionlimit(111111)

t=int(input())
def DFS(x):
    global result
    visit[x]=1
    res.append(x)
    students=student[x]
    if visit[students]==1:
        if students in res:
            result += res[res.index(students):]
        return
    else:
        DFS(students)
for _ in range(t):
    n=int(input()) 
    tmp=0
    student=list(map(int, input().split()))
    student.insert(0,0)
    visit=[0]*(n+1)
    visit[0]=1
    result=[]
    for i in range(1, len(student)):
        if visit[i]==0:
            res=[]
            DFS(i)
        
    print(n-len(result))

    


    