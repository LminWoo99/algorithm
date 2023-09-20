# from itertools import combinations

# card_num, target_num = map(int, input().split())
# card_list = list(map(int, input().split()))
# biggest_num = 0

# for cards in combinations(card_list, 3):
#    temp_sum = sum(cards)
#    if biggest_num < temp_sum <= target_num:
#        biggest_num = temp_sum
# print(biggest_num)
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k]>M:
                continue
            else:
                 result = max(result, arr[i]+arr[j]+arr[k])
print(result)
                