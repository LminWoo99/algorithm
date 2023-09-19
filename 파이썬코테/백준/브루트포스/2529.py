import sys
input=sys.stdin.readline

k=int(input())
a=list(input().split())

visit=[0]*10
max_ans=""
min_ans=""
def check(i,j,k):
    if k=="<":
        return i<j
    else:
        return i>j
def solve(depth, s):
    global max_ans, min_ans
    if depth==(k+1):
        if len(min_ans)==0:
            min_ans=s
        else:
            max_ans=s
        return
    for i in range(10):
        if not visit[i]:
            if(depth==0 or check(s[-1], str(i), a[depth-1])):
                visit[i]=True
                solve(depth+1, s+str(i))
                visit[i]=False
solve(0, "")
print(max_ans)
print(min_ans)
