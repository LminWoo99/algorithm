import sys
sys.setrecursionlimit(10**8)
dists={'d':(1,0), 'l':(0,-1),  'r':(0,1), 'u':(-1,0) }
answer = 'z'
def DFS(n, m, x, y, r, c,cnt,  k):
    global answer
    if k<len(cnt)+abs(x-r)+abs(y-c):
        return
    if x==r and y==c and len(cnt)==k:
        answer=cnt
        return
    for dct, dist in dists.items():
        if 1<=x+dist[0]<=n and 1<=y+dist[1]<=m and cnt<answer:
            DFS(n,m,x+dist[0],y+dist[1], r,c, cnt+dct, k)
def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    DFS(n,m,x,y,r,c,'', k)
    return answer

print(solution(3,4,2,3,3,1,5))

