import sys
input = sys.stdin.readline

def check(temp, sticker):
    for xx in range(len(sticker)):
        for yy in range(len(sticker[0])):
            if temp[i+xx][j+yy]+sticker[xx][yy]>1:
                return False
    return True
def attach(temp, sticker):
    for xx in range(len(sticker)):
        for yy in range(len(sticker[0])):
            temp[i+xx][j+yy]+=sticker[xx][yy]
    return
def rotate(arr):
    n, m = len(arr), len(arr[0])
    result=[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=arr[i][j]
    return result

            
Y, X, k = map(int, input().split())
notebook = [[0] * X for _ in range(Y)]
for _ in range(k):
    y,x =map(int, input().split())
    sticker=[list(map(int, input().split())) for _ in range(y)]
    chk=False
    cnt=0
    while cnt<4:
        if chk==True:
            break
        for i in range(Y-len(sticker)+1):
            if chk==True:
                break
            for j in range(X-len(sticker[0])+1):
                if check(notebook, sticker):
                    attach(notebook, sticker)
                    chk=True
                    break
        sticker=rotate(sticker)
        cnt+=1
answer = 0
for i in range(Y):
    for j in range(X):
        answer += notebook[i][j]

print(answer)