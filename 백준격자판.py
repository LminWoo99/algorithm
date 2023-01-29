n=int(input())
temp=list([0]*n)
def check(a):
    res=list([0]*n)
    one=1
    zero=0
    for i in range(n):
        he=format(int(temp[i]), 'x')
        if a[i][::-1]==a[i] or he==he[::-1]:
            res[i]=one
        else:
            res[i]=zero
    return res    
        
for i in range(n):
    temp[i]=input()
for i in range(n):
    print(check(temp)[i])