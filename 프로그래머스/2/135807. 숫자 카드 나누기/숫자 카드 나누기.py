import math

def GCD(x):
    if len(x) == 0:
        return 0
    result = x[0]
    for i in range(1, len(x)):
        result = math.gcd(result, x[i])
    return result

def solution(arrayA, arrayB):
    answer = 0
    tmpA = GCD(arrayA)
    tmpB = GCD(arrayB)  # arrayB로 수정
    flagA = True
    flagB = True
    
    for arr in arrayB:
        if arr % tmpA == 0:
            flagA = False
            break
    
    for arr in arrayA:
        if arr % tmpB == 0:
            flagB = False
            break
    
    if flagA:
        answer = max(answer, tmpA)
    if flagB:
        answer = max(answer, tmpB)
    
    return answer