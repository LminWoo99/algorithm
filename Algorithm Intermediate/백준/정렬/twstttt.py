import sys
input=sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
dp = {}
def DFS(now, visit):
    if visit == (1 << N) - 1:
        if board[now][0]:
            return board[now][0]
        else:
            return int(1e9)
    if (now, visit) in dp:
        return dp[(now, visit)]
    res = sys.maxsize
    for next in range(1, N):
        if board[now][next] == 0 or visit & (1 << next):
            continue
        cost = DFS(next, visit | (1 << next)) + board[now][next]
        res = min(cost, res)

    dp[(now, visit)] = res  
    return res  


print(DFS(0, 1))