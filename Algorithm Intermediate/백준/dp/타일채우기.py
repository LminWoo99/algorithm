def s(n,m):
    answer=0
    tmp=0
    for i in range(n,m+1):
        i=str(i)
        tmp=i[::-1]
        if tmp==i:
            answer+=1
    return answer
n,m=map(int, input().split())
print(s(n,m))