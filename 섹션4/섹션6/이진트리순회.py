def DFS(n):
    if n>7:
        return
    else:
        DFS(n*2)
        DFS(n*2+1)
        print(n, end=' ')
DFS(1)
