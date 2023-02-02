n=input()
stack=[]
res=''
for x in n:
    if x.isdecimal()==True:
        stack.append(int(x))
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n1+n2)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=="*":
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=="/":
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])
            
        