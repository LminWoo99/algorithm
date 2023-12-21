n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def solution(road):
    global n, l
    visited = [0] * n
    for i in range(n - 1):
        if road[i] != road[i + 1]:
            if abs(road[i] - road[i+1]) > 1 :
                return False
            else:
                if road[i] - road[i + 1] == 1:
                    if i+1+l > n:
                        return False
                    check = road[i + 1]
                    for j in range(i+1, i+1+l):
                        if visited[j] or road[j] != check:
                            return False
                        visited[j] = 1
                elif road[i] - road[i + 1] == -1:
                    if i - l < - 1:
                        return False
                    check = road[i]
                    for j in range(i, i-l, -1):
                        if visited[j] or road[j] != check:
                            return False
                        visited[j] = 1
    return True

result = 0
for row in arr:
    if solution(row):
        result += 1

for columns in range(n):
    if solution( [arr[row][columns] for row in range(n)]):
        result += 1

print(result)