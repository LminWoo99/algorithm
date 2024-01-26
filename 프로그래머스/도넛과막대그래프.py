def solution(edges):
    answer = [0, 0, 0, 0]

    graph = {}
    for a, b in edges:
        if not graph.get(a):
            graph[a] = [0, 0]
        if not graph.get(b):
            graph[b] = [0, 0]
        graph[a][0] += 1
        graph[b][1] += 1
        print(graph)
    for key, exchangeCnt in graph.items():
        print(key, exchangeCnt)

        if exchangeCnt[0] >= 2 and exchangeCnt[1] == 0:
            answer[0] = key

        elif exchangeCnt[0] == 0 and exchangeCnt[1] > 0:
            answer[2] += 1

        elif exchangeCnt[0] >= 2 and exchangeCnt[1] >= 2:
            answer[3] += 1
    
    answer[1] = (graph[answer[0]][0] - answer[2] - answer[3])

    return answer
edge=[[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edge))