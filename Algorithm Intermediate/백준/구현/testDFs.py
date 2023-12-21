def DFS(l):
    if l==2:
        return 2
    DFS(l+1)
x=DFS(0)
print(x)