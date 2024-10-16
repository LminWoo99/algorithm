import sys
input=sys.stdin.readline

n=int(input())
building=list(map(int, input().split()))

## 최대 nlogn으로 풀어야됨
## 후보 : 스택?
res=[[0,0] for _ in range(n)]
right_res=[[0,0] for _ in range(n)]
left_stack=[]
right_stack=[]
## 좌측 부터 구하기
for i in range(n):
    if not left_stack:
        left_stack.append([building[i], i])
    else:
        if left_stack[-1][0]<=building[i]:
            left_stack.pop()
            while left_stack:
                if left_stack[-1][0]<=building[i]:
                    left_stack.pop()
                else:
                    res[i]=[len(left_stack), left_stack[-1][1]]
                    break
            left_stack.append([building[i], i])
        else:
            if left_stack:
                res[i]=[len(left_stack), left_stack[-1][1]]
            left_stack.append([building[i], i])

for i in range(n-1, -1 , -1):
    if not right_stack:
        right_stack.append([building[i], i])
    else:
        if right_stack[-1][0]<=building[i]:
            right_stack.pop()
            while right_stack:
                if right_stack[-1][0]<=building[i]:
                    right_stack.pop()
                else:
                    right_res[i]=[len(right_stack), right_stack[-1][1]]
                    break
            right_stack.append([building[i], i])
        else:
            if right_stack:
                right_res[i]=[len(right_stack), right_stack[-1][1]]
            right_stack.append([building[i], i])
for i in range(n):
    if res[i][0]==0 and right_res[i][0]==0:
        print(0)
    elif res[i][0]!=0 and right_res[i][0]==0:
        print(res[i][0], res[i][1]+1)
    elif res[i][0]==0 and right_res[i][0]!=0:
        print(right_res[i][0], right_res[i][1]+1)
    else:
        x=right_res[i][0]+res[i][0]
        if abs(i-res[i][1])<=abs(i-right_res[i][1]):
            y=res[i][1]
        else:
            y=right_res[i][1]
        print(x,y+1)