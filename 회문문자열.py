n=int(input())
rev=[]
a=list()
b=[0*n]
for i in range(n):
    temp=input()
    temp=temp.upper()
    a.append(temp)
    if(a[i]==temp[::-1]):
        print("%d : YES" %(i+1))
    else:
        print("%d : NO" %(i+1))

    
    
    
