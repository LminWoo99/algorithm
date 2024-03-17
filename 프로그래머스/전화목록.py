def solution(phone_book):
    answer = True
    n=len(phone_book)

    for i in range(n-1):
        if not answer:
            break
        for j in range(i,n):
            if phone_book[j].startswith(phone_book[i])
            answer=False
            break
        
    return answer
solution(["123","456","789"])