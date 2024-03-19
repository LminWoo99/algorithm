def solution(numbers, target):
    n=len(numbers)
    answer = 0
    def DFS(L, cnt):
        if L==n:
            if cnt==target:
                answer+=1
                return
            else:
                return
        for i in range(2):
            if i==0:
                DFS(L+1, cnt+numbers[L])
            else:
                DFS(L+1, cnt-numbers[L])                

    DFS(0,0)
    return answer
solution([1, 1, 1, 1, 1], 3)
    