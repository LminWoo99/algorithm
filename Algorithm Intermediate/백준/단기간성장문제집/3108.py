import sys
input = sys.stdin.readline
def find(node):
    if check[node] != node:
        check[node] = find(check[node])
    return check[node]
def merge(node1, node2):
    rep1 = find(node1)
    rep2 = find(node2)
    check[rep2] = rep1
def meet(rect1, rect2):
    if (rect1[1][0] < rect2[0][0] or rect2[1][0] < rect1[0][0] or
        rect1[0][1] > rect2[1][1] or rect2[0][1] > rect1[1][1]):  
        return False
    elif ((rect1[0][0] < rect2[0][0] < rect2[1][0] < rect1[1][0] and
          rect1[0][1] < rect2[0][1] < rect2[1][1] < rect1[1][1]) or
          (rect2[0][0] < rect1[0][0] < rect1[1][0] < rect2[1][0] and
          rect2[0][1] < rect1[0][1] < rect1[1][1] < rect2[1][1])):
        return False
    else:
        return True
def zero(rect):
    if (0 not in rect[0]) and (0 not in rect[1]):
        return False
    elif rect[0][0]*rect[1][0] > 0 or rect[0][1]*rect[1][1] > 0:
        return False
    else:
        return True
N = int(input())
check = list(range(N))
rects = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    rects.append(((x1, y1), (x2, y2)))

for i in range(N-1):
    for j in range(i+1, N):
        if meet(rects[i], rects[j]):
            merge(i, j)

for i in range(N):
    find(i)
total = len(set(check))
for i in range(N):
    if zero(rects[i]):
        total -= 1
        break

print(total)