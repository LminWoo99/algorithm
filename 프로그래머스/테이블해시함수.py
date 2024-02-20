def solution(data, col, row_begin, row_end):
    answer = 0
    a=[]
    data.sort(key=lambda x:(x[col-1], -x[0]))
    for i in range(row_begin-1, row_end):
        cnt=0
        for j in range(len(data[i])):
            cnt+=data[i][j]%(i+1)
        
        a.append(cnt)
    for i in a:
        answer=answer^i
    
    return answer