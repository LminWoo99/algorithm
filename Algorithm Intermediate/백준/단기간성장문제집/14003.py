import sys
input = sys.stdin.readline

_ = input()
a = list(map(int, input().split()))
def solution(lis_arr, temp): 
    start = -1 
    end = len(lis_arr)

    while start +1 < end:
        mid = (start + end)//2 

        if temp > lis_arr[mid]: 
            start = mid
        else:
            end = mid
    return end
lis_arr = [-1000000001]
lis_total = [(-1000000001,0)] 
a = a[::-1] 
while a:
    temp = a.pop()
    if temp > lis_arr[-1]:
        lis_total.append((temp, len(lis_arr)))
        lis_arr.append(temp)
    else:
        idx = solution(lis_arr, temp)
        lis_arr[idx] = temp
        lis_total.append((temp, idx))
lis_length = len(lis_arr)-1
lis = []
while lis_total and lis_length:
    temp, idx = lis_total.pop()
    if idx == lis_length:
        lis.append(temp)
        lis_length -= 1

print(len(lis))
print(*lis[::-1])