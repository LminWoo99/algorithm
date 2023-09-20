n=input()
stack=[]
cnt=0
for x in range(len(n)):
    if n[x]=='(':
        stack.append(n[x])
    else:
        stack.pop()
        if n[x-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)
        
