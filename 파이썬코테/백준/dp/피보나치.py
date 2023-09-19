import sys
a=int(sys.stdin.readline())
d=[[0,0]]*41
d[0]=[1,0]
d[1]=[0,1]
d[2]=[1,1]
for j in range(a):
    tmp=int(sys.stdin.readline())
    if tmp<3:
        print(d[tmp][0], d[tmp][1])
    else:
        for i in range(3, tmp+1):
            d[i]=[d[i-2][0]+d[i-1][0], d[i-2][1]+d[i-1][1]]
        print(d[tmp][0], d[tmp][1])
    
# 0  1,0
# 1  0,1
# 2  1, 1
# 3  1, 2
# 4  2, 3
# 5  3, 5
