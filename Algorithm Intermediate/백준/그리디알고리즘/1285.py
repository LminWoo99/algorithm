import sys
input=sys.stdin.readline

n=int(input())
a=list(input().rstrip() for _ in range(n))
rev_a=[k[:] for k in a]
print(a)
print(rev_a)
print(1<<3)
res=0

# for i in range(n):
#     for j in range(n):
#         if a[i][j]=="T":
#             res+=1

