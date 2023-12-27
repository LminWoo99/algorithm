import sys
input=sys.stdin.readline

game=list(map(int, input().split()))
a=[0,0,0,0]
board = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]
res=0
def DFS(L, total, horses):
    global res
    if L==10:
        res=max(total, res)
        return
    for i in range(4):
        x=horses[i]
        if len(board[x])==2:
            x=board[x][1]
        else:
            x=board[x][0]
        for _ in range(1, game[L]):
            x=board[x][0]
        if x==32 or (x<32 and x not in horses):
            before=horses[i]
            horses[i]=x
            DFS(L+1, total+score[x], horses)
            horses[i]=before
DFS(0,0,a)
print(res)
        