N=int(input())
expression=list(input())
num=[int(input()) for i in range(N)]
stk=[]
for i in expression:
    if i.isalpha():
        stk.append(num[ord(i)-65])
    else:
        a=stk.pop()
        result=stk.pop()
        if i=='+':
            result+=a
        elif i=='-':
            result-=a
        elif i=='*':
            result*=a
        elif i=='/':
            result/=a
        stk.append(result)
print('%.2f' %stk[-1])
