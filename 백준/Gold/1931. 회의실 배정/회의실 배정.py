import sys
input=sys.stdin.readline
n=int(input())

rooms=[]
for _ in range(n):
    x,y=map(int, input().split())
    rooms.append([x,y])
rooms.sort(key=lambda x:(x[1],x[0]))
res=0
cur_end=0
for i in range(n):
    if cur_end<=rooms[i][0]:
        cur_end=rooms[i][1]
        res+=1
print(res)