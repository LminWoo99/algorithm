from collections import defaultdict, Counter
def solution(tickets):
    answer = []
    paths=defaultdict(list)

    for ticket in tickets:
        paths[ticket[0]].append(ticket[1])
    for path in paths:
        paths[path].sort()
    check=defaultdict(int)
    for path in paths:
        for dest in paths[path]:
            tmp=path+' '+dest
            check[tmp]=0
    print(check)
    def DFS(airport):
        if not paths[airport]:
            return 
        print(answer)
        for dest in paths[airport]:
            print(dest)
            answer.append(dest)
            DFS(dest)
    answer.append('ICN')
    # DFS('ICN')
    print(answer)
    return answer
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])