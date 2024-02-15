# # # def solution(numbers):
# # #     answer = []
# # #     def check_binary(x):
# # #         returnX=""
# # #         while x>=1:
# # #             tmp=str(x%2)
# # #             returnX+=tmp
# # #             x//=2
# # #         return returnX
            
# # #     for i in range(len(numbers)):
# # #         print(check_binary(numbers[i]))
# # #     return answer
# # # solution([7, 42, 5])
# # def check_digit(x):
# #     n=1
# #     while True:
# #         if 2**n-1>x:
# #             return 0
# #         if 2**n-1==x:
# #             return 1
# #         n+=1
# # print(check_digit(31))
# # # 0101010
# # # 1011111
# # # 111
# # # 루트노드는 0이면 안됨
# # 01010
# # 42/2=21
# # 21/2=10
# # 10/2=5
# # 5/2=2
# # 2/2=1
# # 1/1

# print(bin(5)[2:])
binary_num="123"
binary_num="0"+binary_num
print(binary_num)