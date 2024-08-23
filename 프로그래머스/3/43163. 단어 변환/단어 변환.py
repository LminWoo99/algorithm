from collections import deque, defaultdict
def solution(begin, target, words):
    answer=0
    graph=defaultdict(list)
    if target not in words:
        return answer
    words.append(begin)
    for word in words:
        for i in range(len(words)):
            if word!=words[i]:
                cnt=0
                for k in range(len(word)):
                    if word[k]!=words[i][k]:
                        cnt+=1
                if cnt<=1:
                    graph[word].append((words[i],i))
    def BFS(start):
        visit=[0]*len(words)
        dq=deque()
        dq.append((start,0))
        while dq:
            x,res=dq.popleft()
            if x==target:
                return res
            for a in graph[x]:
                next_word, next_idx=a[0], a[1]
                if not visit[next_idx]:
                    visit[next_idx]=1
                    dq.append((next_word, res+1))
        return 0
    answer=BFS(begin)
    return answer

    
    ## 우선 현재에서 바꿀수있는거 dq에 다 넣는다
    ## 현재 바꿀수있는거를 어떻게 체크할건지 ==> for문,  미리 하나 찾아서 그래프 만들자
    
    ## visit을 2차원 배열로 만들고 