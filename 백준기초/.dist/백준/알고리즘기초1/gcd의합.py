import math
n=int(input())
res=[]
for i in range(n):
    temp_sum=0
    res=list(map(int, input().split()))
    for j in range(1, len(res)):
        for k in range(j+1, len(res)):
            temp_sum+=math.gcd(res[j], res[k])
    print(temp_sum)
    
   
    
