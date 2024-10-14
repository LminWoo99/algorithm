def solution(cookie):
    n=len(cookie)
    ##과자수 같아야함
    cookie_sum=cookie[:]
    for i in range(1,n):
        cookie_sum[i]+=cookie_sum[i-1]
    answer=0
    ## 가운데 피봇을 잡음
    ## 피봇이란 ? -> m
    ## start, end를 잡고 왼쪽부분이 더 크면 start+=1
    ## end가 더크면 end-=1
    for i in range(n-1):
        start,end=0, n-1
        mid=i
        left, right=0,0
        while start<=mid and mid<end:
            # if mid==start:
            #     left=cookie[mid]
            #     right=cookie_sum[end]-cookie_sum[mid]
            # else:
            left=cookie_sum[mid]-cookie_sum[start]+cookie[start]
            right=cookie_sum[end]-cookie_sum[mid]
            if left==right:
                answer=max(answer, left)
                break
            elif left>right:
                start+=1
            elif left<right:
                end-=1
    return answer