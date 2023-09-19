# n=list(input())
# tmp=0
# for i in range(len(n)-1, -1 ,-1):
#     n[i]=int(n[i])
#     if n[i]==1:
#         tmp+=2**(len(n)-i-1)
# tmp=str(tmp)
# temp=0
# res=[]
# for i in range(len(tmp)):
#     tmp=int(tmp)
#     res.append(tmp%8)
#     tmp=tmp//8
# res.reverse()
# for i in res:
#     print(i, end='')

print(oct(int(input(),2))[2:])
print(bin(int(input(),8))[2:])
