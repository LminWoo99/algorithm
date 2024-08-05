from itertools import permutations
import math

def isPrime(target):
    if target <= 1:
        return False
    if target == 2:
        return True
    for i in range(2, int(math.sqrt(target)) + 1):
        if target % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    cand = [num for num in numbers]  # numbers를 하나씩 나눠서 리스트
    isPrime_list = set()

    def DFS(tmp, used):
        if tmp:
            isPrime_list.add(int(tmp))
        for i in range(len(cand)):
            if not used[i]:
                used[i] = True
                DFS(tmp + cand[i], used)
                used[i] = False

    DFS("", [False] * len(cand))
    
    for num in isPrime_list:
        if isPrime(num):
            answer.add(num)

    return len(answer)


# def solution(numbers):
#     ## 완탐 가능할듯
#     answer=set()
#     cand=[num for num in numbers]

#     ## 순열로 소수인지 파악
#     for i in range(1, len(cand)+1):
#         for j in permutations(cand, i):
#             tmp=int(''.join(j))
#             if isPrime(tmp):
#                 answer.add(tmp)
#     return len(answer)
