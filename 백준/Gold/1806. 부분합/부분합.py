import sys
input=sys.stdin.readline

n,m=map(int, input().split())
a=list(map(int, input().split()))

res=sys.maxsize
tmp_plus=0
left,right=0,0
while True:
    if tmp_plus >= m:
        res=min(res, right-left)
        tmp_plus-=a[left]
        left+=1
    elif right==n:
        break
    else:
        tmp_plus+=a[right]
        right+=1
if res==sys.maxsize:
    print(0)
else:
    print(res)
        
    
        
        
