
import sys
input=sys.stdin.readline
## 내답
# def solution(n):
#     n=str(n)
#     cou=False
#     for x in range(len(n)-2):
#         if n[x]=='6' and n[x+1]=='6' and n[x+2]=='6':
#             cou=True
#     return cou
n=int(input())
star=[]
tmp=1
i=666
# while True:
#     if tmp==n:
#         break
#     else:
#         i+=1
#         if solution(i):
#             tmp+=1
         
# print(i)
        
        
    
## 다른 사람 답 참고
while True:
    if tmp==n:
        break
    else:
        i+=1
        if '666' in str(i):
            tmp+=1
print(i)