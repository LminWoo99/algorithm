from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    check=defaultdict(str) #입출차 체크
    results=[]
    for record in records:
        x,y,z=record.split(' ')
        x_arr=x.split(':')
        if check[y]:
            tmp=int(x_arr[0])*60+int(x_arr[1])
            results.append((tmp-check[y], y))
            del(check[y])
        else:
            check[y]=int(x_arr[0])*60+int(x_arr[1])
    if check:
        for chk in check:
            temp=1439-check[chk]
            results.append((temp, chk))
    tmp_answer=defaultdict(str)
    for result in results:
        if result[1] not in tmp_answer.keys():
            tmp_answer[result[1]]=result[0]
        else:
            tmp_answer[result[1]]+=result[0]
    tmp_answer=sorted(tmp_answer.items())
    print(tmp_answer)
    for ans in tmp_answer:
        if ans[1]>fees[0]:
            answer.append(math.ceil(((ans[1]-fees[0])/fees[2]))*fees[3]+fees[1])
        else:
            answer.append(fees[1])
    return answer
print(solution([180, 5000, 10, 600], ["16:00 3961 IN", "17:00 3961 OUT", "17:10 3961 IN"]))

# 