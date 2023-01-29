'''
n=int(input())
a=list(input().split())

def reverse(x):
    b=list()
    for i in x:
        b.append(i[::-1])
    b=list(map(int, b))
    return isPrime(b)    
def isPrime(x):
    temp=list()
    for i in x:
        for j in range(2,i):    
            if i%j==0:
                break
        else:
            temp.append(i)
    return temp            
result=reverse(a)
for k in result:
    print(k, end=' ')
''' #두가지 방법

n=int(input())
a=list(map(int, input().split()))
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True

for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')



                 