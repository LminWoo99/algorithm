import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ab_sum=[]
cd_sum=[]
for i in range(n):
    for j in range(n):
        ab_sum.append(a[i][0]+a[j][1])
        cd_sum.append(a[i][2]+a[j][3])
ab_sum.sort()
cd_sum.sort()

left ,right=0, len(ab_sum)-1
res=0
while left<len(ab_sum) and right>=0:
    if ab_sum[left]+cd_sum[right]==0:
        next_left, next_right=left+1, right-1
        while next_left<len(ab_sum) and ab_sum[left]==ab_sum[next_left]:
            next_left+=1
        while next_right>=0 and cd_sum[next_right]==cd_sum[right]:
            next_right-=1
        res+=(next_left-left)*(right-next_right)
        left,right=next_left,next_right
    elif ab_sum[left]+cd_sum[right]>0:
        right-=1
    else:
        left+=1
print(res)