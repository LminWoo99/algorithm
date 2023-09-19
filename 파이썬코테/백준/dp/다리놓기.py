# import sys
# import math
# n=int(sys.stdin.readline())
# for i in range(n):
#     a,b=map(int, sys.stdin.readline().split())
#     bridge=math.factorial(b)//(math.factorial(a)*math.factorial(b-a))
#     print(bridge)
interval=[[1,3], [1,4], [4,5]]
s="abcde"
for i in interval:
    a=a[i[0]-1:i[1]].reverse
    a=a[::-1]+s[i[1]:]
    print(a)