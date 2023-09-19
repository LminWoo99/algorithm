import sys
t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    d=[i for i in range(1, n+1)]
    for j in range(k):
        for x in range(1, n):
            d[x]+=d[x-1]
    print(d[-1])
