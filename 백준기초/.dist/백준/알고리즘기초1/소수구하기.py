def isPrime(a):
    if a==1:
        return False
    else:
        for i in range(2, int(a**0.5)+1):
            if a%i==0:
                return False
        return True
 
            
m,n=map(int, input().split())
res=[]
for i in range(m,n+1):
    if isPrime(i):
        res.append(i)


for i in res:
    print(i)
