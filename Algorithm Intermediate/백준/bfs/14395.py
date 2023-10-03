from collections import deque

s, t = map(int, input().split())
q = deque()
visited = set()
if s == t:
    print(0)
elif t == 1:
    print('/')
else:
    q.append([s, ''])
    visited.add(s)
    while q:
        x, y = q.popleft()
        if x == t:
            print(y)
            break
        else:
            if x ** 2 <= 10**9 and x**2 not in visited:
                visited.add(x**2)
                q.append([x**2, y+'*'])
            if x * 2 <= 10**9 and x*2 not in visited:
                visited.add(x*2)
                q.append([x*2, y+'+'])
            if x / x not in visited:
                visited.add(1)
                q.append([1, y+'/'])
    else:
        print(-1)
        # 적합한 연산이 없을 경우 -1을 출력해줍니다.