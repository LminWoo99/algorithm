from collections import defaultdict
def solution(genres, plays):
    answer = []
    n=len(genres)
    a=defaultdict(list)

    for i in range(n):
        a[genres[i]].append((plays[i],i))

    tmp= sorted(a.values(), key=lambda x: sum(item[0] for item in x), reverse=True)
    for i in tmp:
        if len(i)==1:
            answer.append(i[0][1])
        else:
            i.sort(key=lambda x:(-x[0], x[1]))
            for j in range(2):
                answer.append(i[j][1])

    return answer