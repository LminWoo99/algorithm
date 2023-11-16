from sys import stdin
input = stdin.readline
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
changeDir = ((2, 3), (2, 3), (0, 1), (0, 1))

def bfs():
    check = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    for sr, sc, sd in Q:
        check[sr][sc][sd] = 0
    while Q:
        r, c, d = Q.popleft()
        nr = r + dr[d]
        nc = c + dc[d]
        # 격자 밖이거나 벽이면
        if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":
            continue
            
        # 빈 공간인 경우
        if A[nr][nc] == ".":
            if check[nr][nc][d] == -1:      # 첫 방문
                check[nr][nc][d] = check[r][c][d]
                Q.append((nr, nc, d))
            else:     # 이미 방문했다면 갱신할 수 있는 경우에만
                if check[nr][nc][d] > check[r][c][d]:
                    check[nr][nc][d] = check[r][c][d]   # 최솟값 갱신
                    Q.append((nr, nc, d))
                    
        # 거울 설치할 수 있는 경우
        elif A[nr][nc] == "!":
            # 거울 설치 X
            if check[nr][nc][d] == -1:      # 첫 방문
                check[nr][nc][d] = check[r][c][d]
                Q.append((nr, nc, d))
            else:     # 이미 방문했다면 갱신할 수 있는 경우에만
                if check[nr][nc][d] > check[r][c][d]:
                    check[nr][nc][d] = check[r][c][d]   # 최솟값 갱신
                    Q.append((nr, nc, d))
            # 거울 설치 O
            for nd in changeDir[d]:
                print(nd)
                if check[nr][nc][nd] == -1:     # 첫 방문
                    check[nr][nc][nd] = check[r][c][d] + 1
                    Q.append((nr, nc, nd))
                else:     # 이미 방문했다면 갱신할 수 있는 경우에만
                    if check[nr][nc][nd] > check[r][c][d] + 1:      # 최솟값 갱신
                        check[nr][nc][nd] = check[r][c][d] + 1
                        Q.append((nr, nc, nd))

    temp = []   # 가능한 경우의 수
    for chk in check[gr][gc]:
        if chk == -1:
            continue
        temp.append(chk)
    return min(temp)

# main
N = int(input())
A = []
doors = []
for i in range(N):
    A.append(list(input().strip()))
    for j in range(N):
        if A[i][j] == "#":
            doors.append([i, j])
            A[i][j] = "."

sr, sc = doors[0]   # 시작 좌표
gr, gc = doors[1]   # 도착 좌표

Q = deque()
for d in range(4):
    nr = sr + dr[d]
    nc = sc + dc[d]
    if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":
        continue
    Q.append((sr, sc, d))   # 시작 가능한 방향 모두 큐에 담기

print(bfs())