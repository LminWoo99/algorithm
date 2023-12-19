import sys
input=sys.stdin.readline
def solve(i, cnt):
    flag=True
    global result

    back=-10
    if cnt<=1:
        for x in range(len(i)-1):
            
            if i[x]!=i[x+1]:
                if abs(i[x]-i[x+1])!=1:
                    flag=False
                    break
                else:
                    # if back+l==x:
                    #     print(i, back)
                    #     flag=False
                    #     break
                    # else:
                        
                        if x+l+1<=len(i)-1:
                            
                            for j in range(x+1, x+l+1):
                                if i[j]!=i[j+1]:
                                   
                                    flag=False
                                    break
                                else:
                                    print(i, back)
                                    back=j
                        
                        else:
                            flag=False
                            break

        if flag:
            print(i)
            result+=1
            return
        # else:
        #     i=i[::-1]
        #     solve(i, cnt+1)]
    
    return 0        
        
n,l=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]
result=0
for i in board:
    solve(i, 0)
for i in range(n):
    j=list(zip(*board))[i]
    solve(j, 0)


print(result)
