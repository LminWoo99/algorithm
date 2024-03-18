from itertools import product
def solution(word):
    answer = 0
    alpha={'A':"1", "E":"2", "I":"3", "O":"4", "U":"5"}
    change=""
    for i in range(len(word)):
        change+=alpha[word[i]]
    target=[]
    permu=["1", "2", "3", "4", "5"]
    for i in range(1, 6):
        for x in product(permu, repeat=i):
            x=''.join(x)
            target.append(x)
    target=sorted(target)
    answer=target.index(change)+1
    return answer