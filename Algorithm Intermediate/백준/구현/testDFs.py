def DFS(L):
    if  L==3:
        print("wow")
        return
    else:
        DFS(L+1)
        print("heello")
DFS(0)