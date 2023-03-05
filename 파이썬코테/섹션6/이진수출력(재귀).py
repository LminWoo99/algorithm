

def DfS(n):
    x=1
    res=0
    if n>=1:
        res=(n%2)
        DfS(n//2)
        print(res, end='')
    
n=int(input())
DfS(n)
