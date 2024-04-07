import sys
input = sys.stdin.readline
h,w=map(int, input().split())
block=list(map(int, input().split()))

res=0
for i in range(1, w-1):
   left=max(block[:i])
   right=max(block[i+1:])
   tmp=min(left, right)
   if block[i]<tmp:
       res+=tmp-block[i]
print(res)