import sys
from collections import deque
from itertools import permutations

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j):
    visited = [[0] * w for _ in range(h)]
    visited[i][j] = 1
    queue = deque([(i, j)])
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                if maps[nr][nc] != 'x':
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    return visited


while True:
    w, h = map(int, input().split())
    if w + h:
        maps = [list(''.join(map(str, sys.stdin.readline().rstrip()))) for _ in range(h)]
        dirty = [] # 더러운 칸의 좌표를 담을 배열
        cr, cc = 0, 0 # 로봇 청소기의 위치(행, 열)
        for r in range(h):
            for c in range(w):
                if maps[r][c] == 'o':
                    cr, cc = r, c
                elif maps[r][c] == '*':
                    dirty.append((r, c))

        cleaner = [0] * len(dirty) # 로봇 청소기 ~ 첫 번째로 청소할 더러운 칸까지의 거리를 담을 배열
        visited = bfs(cr, cc)
        is_possible = True # 로봇 청소기가 모든 더러운 칸을 방문할 수 있는지 확인
        for idx, rc in enumerate(dirty):
            tmp = visited[rc[0]][rc[1]]
            if not tmp: # 로봇 청소기가 방문할 수 없는 칸이 나오면 False
                print(-1)
                is_possible = False
                break
            cleaner[idx] += tmp - 1 

        if is_possible:
            dist = [[0] * (len(dirty)) for _ in range(len(dirty))] # 더러운 칸마다의 거리를 계산한다.
            for i in range(len(dirty) - 1):
                visited = bfs(dirty[i][0], dirty[i][1])
                for j in range(i + 1, len(dirty)):
                    dist[i][j] = visited[dirty[j][0]][dirty[j][1]] - 1
                    dist[j][i] = dist[i][j]
            answer = int(1e9)
            for li in permutations(range(len(dist))): # 순열을 이용하여 최적의 순서를 찾는다.

                tmp = cleaner[li[0]]
                start = li[0]
                for idx in range(1, len(li)): # 순열을 기준으로 시작점(start), 도착점(end)을 바꿔가며 거리를 더한다. 
                    end = li[idx]
                    tmp += dist[start][end]
                    start = end
                answer = min(answer, tmp) # answer에 이동횟수의 최소값을 담는다.
            print(answer)
    else:
        break 