exp=input()
stack=[]
res=''
for i in exp:
    if i.isalpha()==True:
        res+=i
    else:
        if i=='(':
            stack.append(i)
        elif i=='*' or i=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(i)
        elif i=='+' or i=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
