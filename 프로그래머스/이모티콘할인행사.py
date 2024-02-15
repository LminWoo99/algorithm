# 일정 비율이상이 되야 이뫼콘은 구매
# 구독서비스를 최대한
# 이모티콘 매출액을 최대한(10%, 20%, 30%, 40%)
from itertools import product
subscribe_cnt, sales=0, 0
def solution(users, emoticons):
    answer = []
    discount=[10,20,30,40]
    #구독수, 매출액     
    
    n=len(emoticons)
    def check(cand_list, x,y):
        global subscribe_cnt
        global sales
        for users_dis, users_stan in users:
            tmp=0
            for i in range(len(cand_list)):
                if users_dis<=cand_list[i]:
                    tmp+=(emoticons[i]*(100-cand_list[i]))//100
            if tmp>=users_stan:
                x+=1
            else:
                y+=tmp
        
        if x>subscribe_cnt:
            subscribe_cnt=x
            sales=y
        elif x==subscribe_cnt==x and y>sales:
            sales=y
    for a in product(discount, repeat=n):
        check(list(a), 0, 0)
    answer.append(subscribe_cnt)
    answer.append(sales)
    return answer
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))