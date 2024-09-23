import sys
input=sys.stdin.readline

answer=int(1e9)*3
ans_list=[]
n=int(input())
liquid_list=list(map(int, input().split()))
liquid_list.sort()
for i in range(n-2):
    pin=liquid_list[i]
    start=i+1
    end=n-1
    while start<end:
        val=pin+(liquid_list[start]+liquid_list[end])
        if abs(val)<answer:
            answer=abs(val)
            ans_list=[pin, liquid_list[start],liquid_list[end]]
        if val>0:
            end-=1
        elif val<0:
            start+=1
        else:
            break
        
print(*ans_list)