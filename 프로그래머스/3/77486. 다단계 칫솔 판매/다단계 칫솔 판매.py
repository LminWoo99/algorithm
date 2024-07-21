from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = defaultdict(int)
    sale_amount=[]
    ### 일단 seller, amount for문으로 각자 판매량 구하기
    for i in range(len(seller)):
            sale_amount.append(amount[i]*100)
    graph=defaultdict(list)
    ## enroll순서대로 graph형태로 referral 값 넣기
    for i in range(len(enroll)):
        if referral[i]!='-':
            graph[enroll[i]].append(referral[i])
        answer[enroll[i]]=0
    ## 나중에 판매량 계산할떄 if graph있으면 나눠주고 자기는 남은 금액
    for i in range(len(seller)):
        if graph[seller[i]]:
            cnt=seller[i]
            tmp=sale_amount[i]//10
            answer[cnt]+=sale_amount[i]-tmp
            while True:
                if not graph[cnt]:
                    break                
                cnt=graph[cnt][0]
                answer[cnt]+=tmp-(tmp//10)
                tmp//=10
                if tmp<1:
                    break
        else:
            answer[seller[i]]+=(sale_amount[i]*9)//10
    result=[]
    for ans in enroll:
        result.append(answer[ans])
    return result
