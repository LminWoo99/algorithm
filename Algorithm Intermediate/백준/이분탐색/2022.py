import sys
input=sys.stdin.readline
def get(x,y,width):
    h1=(x**2 - width**2)**0.5
    h2=(y**2 - width**2)**0.5
    c=h1*h2/(h1+h2)
    return c
x,y,c=map(float, input().split())

start, end=0, min(x,y)
res=0
while (end-start)>0.000001:
    width=(end+start)/2
    res=width
    if get(x,y,width)>= c:
        start=width
    else:
        end=width
print(res)