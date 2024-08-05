from itertools import permutations
import math
def isPrime(target):
    if target<=1:
        return False
    if target==2:
        return True
    for i in range(2, int(math.sqrt(target))+1):
        if target%i==0:
            return False
    return True
def solution(numbers):
    ## 완탐 가능할듯
    answer=set()
    cand=[num for num in numbers]

    ## 순열로 소수인지 파악
    for i in range(1, len(cand)+1):
        for j in permutations(cand, i):
            tmp=int(''.join(j))
            if isPrime(tmp):
                print(tmp)
                answer.add(tmp)
    return len(answer)
