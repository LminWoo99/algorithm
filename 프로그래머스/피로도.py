from itertools import permutations
def solution(k, dungeons):
    answer = -1
    n=len(dungeons)
    order=[]
    for i in range(n):
        order.append(i)
    def explore(a):
        res=0
        tmp=k
        for i in range(len(a)):
            if dungeons[a[i]][0]<=tmp:
                tmp-=dungeons[a[i]][1]
                res+=1
            else:
                break
        return res
    for x in permutations(order, n):
        tmp=explore(x)
        answer=max(answer, tmp)
        if answer==n:
            break
    return answer