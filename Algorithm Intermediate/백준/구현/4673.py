def solution(n):
    answer=0
    while n>0:
        answer+=n%10
        n//=10
    return answer
check=[0]*100001

for i in range(1, 100001):
    res=solution(i)
    if res+i<=10000:
        check[res+i]=1
for i in range(1, 10000):
    if check[i]==0:
        print(i)