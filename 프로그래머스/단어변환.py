from collections import deque
def solution(begin, target, words):
    answer = 0
    def BFS(word):
        dq=deque()
        dq.append((word, 0))
        while dq:
            word, cnt=dq.popleft()
            if word==target:
                return cnt
            for i in words:
                num=0
                for j in range(len(i)):
                    if num>1:
                        break
                    if i[j]!=word[j]:
                        num+=1
                if num==1:
                    dq.append((i, cnt+1))
    if target not in words:
        return answer        
    else:
        answer=BFS(begin)
        return answer        
        