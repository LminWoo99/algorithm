import sys
from collections import deque

visited = []
res = 0
def pool():
    global res, visited
    def bfs(x, y, h):
        global res, visited
        que = deque()
        que.append((x,y))
        flag = True  
        visited[x][y] = True
        cnt = 1
        while que:
            x, y = que.popleft()
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if nx == -1 or nx == N or ny == -1 or ny == M:
                    flag = False
                    continue
                if board[nx][ny] <= h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    cnt += 1
        if flag:
            res += cnt

    N, M = map(int, input().split())
    board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

    dx = [-1,0,1,0]
    dy=[0,1,0,-1]
    

    for num in range(1, 9):
        visited = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] <= num and not visited[i][j]:
                    bfs(i, j, num)
    print(res)


pool()
