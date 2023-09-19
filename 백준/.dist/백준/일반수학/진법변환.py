a=''
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split())
# print(int(n,int(b)))
while n!=0:
    a += str(system[n%b])
    n//=b
    
print(a[::-1])