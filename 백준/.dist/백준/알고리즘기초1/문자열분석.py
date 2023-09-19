import sys
while True:
    a=list(sys.stdin.readline().rstrip('\n'))
    if not a:
        break
    else:    
        x,y,z,t=0,0,0,0
        for i in a:
            if i.islower():
                x+=1
            elif i.isupper():
                y+=1
            elif i.isdigit():
                z+=1
            else:
                t+=1
            print(x,y,z,t)