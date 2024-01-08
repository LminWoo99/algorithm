import sys
input=sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
duck = []
target=[]
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            duck.append((i, j))
        elif board[i][j]=='X':
            target.append((i,j))

def spread_water():
    water = deque()
    # for i in range(r):
    #     for j in range(c):
    for i,j in target:
        if board[i][j] == 'X':
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < r and 0 <= nj < c and board[ni][nj] == '.':
                    water.append((i, j))
                    break

    while water:
        x, y = water.popleft()
        board[x][y] = '.'
        
def BFS():
    dq = deque()
    dq.append((duck[0][0], duck[0][1]))
    visited = [[False] * c for _ in range(r)]
    visited[duck[0][0]][duck[0][1]] = True

    while dq:
        x, y = dq.popleft()
        if x == duck[1][0] and y == duck[1][1]:
            return True

        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < r and 0 <= yy < c and not visited[xx][yy] and board[xx][yy] != 'X':
                visited[xx][yy] = True
                dq.append((xx, yy))

    return False

days = 0
while True:
    if BFS():
        break

    spread_water()
    days += 1

print(days)