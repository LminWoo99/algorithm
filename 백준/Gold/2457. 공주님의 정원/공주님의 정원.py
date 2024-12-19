import sys
input=sys.stdin.readline

n=int(input())
flowers_info=[]
for _ in range(n):
    x,y,z,d=map(int, input().split())
    flowers_info.append([x*100+y, z*100+d])

flowers_info.sort()
end_date=301
res=0
while flowers_info:
    if (end_date>=1201 or flowers_info[0][0]>end_date):
        break
    tmp=-1
    for _ in range(len(flowers_info)):
        if (flowers_info[0][0] <= end_date):
            if tmp<=flowers_info[0][1]:
                tmp=flowers_info[0][1]
            flowers_info.remove(flowers_info[0])
        else:
            break
    end_date=tmp
    res+=1
if end_date<1201:
    print(0)
else:
    print(res)