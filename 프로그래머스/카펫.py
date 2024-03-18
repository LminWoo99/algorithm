def solution(brown, yellow):
    answer = []
    n=(brown+4)//2
    print(n)
    for i in range(1, n):
        x=i
        y=n-i
        if (x-2)*(y-2)==yellow:
            width=max(x,y)
            height=min(x,y)
            answer.append(width)
            answer.append(height)
            break
    
    return answer



