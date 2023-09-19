import sys
input=sys.stdin.readline
a=set()
def calculator(name, x):
    global a
    if name=="add":
        a.add(x)
    elif name=="remove":
        a.discard(x)
    elif name=="check":
        if x in a:
            print(1)
        else:
            print(0)
    elif name=="toggle":
        if x in a:
           a.remove(x)
        else:
            a.append(x)
    elif name=="all":
        a=[]
        for i in range(1,21):
            a.add(i)
    else:
        a=set()
m=int(input())
for i in range(m):
    a=input().split()
    calculator(a[0],a[1])