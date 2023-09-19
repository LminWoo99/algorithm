def DFS(L, idx):
    if L==6:
        print(*res)
        return
    
    for i in range(idx, k):
        res.append(s[i])
        DFS(L+1, i+1)
        res.pop()
            
while True:
    
    a=list(map(int, input().split()))
    k=a[0]
    s=a[1:]
    res=[]
    DFS(0, 0)
    if k==0:
        break
    print()
        