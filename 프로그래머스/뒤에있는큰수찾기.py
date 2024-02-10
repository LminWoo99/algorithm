# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)-1):
#         flag=False
#         for j in range(i+1, len(numbers)):
#             if numbers[i]<numbers[j]:
#                 answer.append(numbers[j])
#                 flag=True
#                 break
#         if not flag:
#             answer.append(-1)        
#     answer.append(-1)
#     return answer



# # 4 2 4 -1
# # wrong = 4 4 4 -1

a=[1,2,3,4]
sorted(a, reverse=True)
print(a)