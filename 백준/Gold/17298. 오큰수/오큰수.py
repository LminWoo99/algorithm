import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
res=[-1]*n
stack=[0]

for i in range(1, n):
    # 오큰수 : A[i]의 오른쪽에 있으면서 A[i]보다 큰 수 중 가장 왼쪽 값 
    while stack and a[stack[-1]] < a[i]:
        res[stack.pop()] = a[i] # 해당 인덱스 칸은 A[i]
    stack.append(i)
print(*res)

    