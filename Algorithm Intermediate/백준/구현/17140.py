import sys
input=sys.stdin.readline
def line(a):
    max_tmp=0
    for i in range(len(a)):
        check=[0]*101
        tmp=[]
        for j in a[i]:
            check[j]+=1
        for k in range(1, 101):
            if check[k]!=0:
                tmp.append((k, check[k]))
        tmp.sort(key=lambda x:(x[1], x[0]))
        max_tmp=max(max_tmp, len(tmp))
    
        a[i]=tmp
    max_tmp*=2
    result=[]
    for i in a:
        new_a=[]
        for j in i:
            new_a.extend(j)
        if len(new_a)<max_tmp:
            new_a.extend([0]* (max_tmp-len(new_a)))
        result.append(new_a)
    return result

    
r,c,k=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(3)]
cnt=0
while True:
    if len(a)>=r and len(a[0])>=c and a[r-1][c-1]==k:
            print(cnt) 
            break
    elif cnt>100:
        print(-1)
        break
    else:
        cnt+=1
        ## 행의 갯수

        line_len=len(a)
        row_len=len(a[0])
        if line_len>=row_len:
            a=line(a)
        else:
            a=list(map(list, zip(*a)))
            a=line(a)
            a=list(map(list, zip(*a)))

