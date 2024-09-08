def divide(a):
    left,right=0,0
    u,v='',''
    for i in range(len(a)):
        if a[i]==')':
            left+=1
        else:
            right+=1
        if left and right:
            if left==right:
                u=a[:i+1]
                v=a[i+1:]
                break
    return u,v
def check_correct(a):
    stack=[]
    if not a:
        return False
    for i in range(len(a)):
        if stack:
            if stack[-1]+a[i]=='()':
                stack.pop()
            else:
                stack.append(a[i])
        else:
            stack.append(a[i])
    if not stack:
        return True
    else:
        return False
def solution(p):
    answer = ''
    if not p:
        return ''
    else:
        u,v=divide(p)
        if check_correct(u):
            return u+solution(v)
        else:
            answer='('
            answer+=solution(v)
            answer+=')'
            for i in u[1: len(u)-1]:
                if i=='(':
                    answer+=')'
                else:
                    answer+='('
            return answer        
    return answer