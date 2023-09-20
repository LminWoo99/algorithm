res=0
temp=0
for i in range(20):
    a,b,c=map(str, input().split())
    b=float(b)
    if c=='A+':
        res+=b*4.5
        temp+=b
    elif c=='A0':
        res+=b*4.0
        temp+=b
    elif c=='B+':
        res+=b*3.5
        temp+=b
    elif c=='B0':
        res+=b*3.0
        temp+=b
    elif c=='C+':
        res+=b*2.5    
        temp+=b
    elif c=='C0':
        res+=b*2.0
        temp+=b
    elif c=='D+':
        res+=b*1.5
        temp+=b
    elif c=='D0':
        res+=b*1.0
        temp+=b
    elif c=='F':
        res+=b*0
        temp+=b
    elif c=='P':
        temp+=0
print("{:.6f}".format(res/temp))        
          
