import math
def solution(n, k):
    answer = 0
    result=digit_change(n,k)
    arr=result.split('0')
    for i in arr:
        if i!='':
            if is_prime(i):
                answer+=1
    return answer
def digit_change(x,y):
    result=""
    while True:
        if x<=1:
            if x==0:
                break
            else:
                result+=str(x)
                break
        result+=str(x%y)
        x//=y
    result=result[::-1]
    return result
def is_prime(x):
    x=int(x)
    if x==2:
        return True
    elif x==1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
print(solution(110011, 10))