def solution(numbers):
    answer = []
    def dfs(b, i, depth):
        if depth==0:
            return True
        if b[i]=="0" and (b[i-depth]=="1" or b[i+depth]=="1"):
            return False
        # 왼쪽 서브트리
        left=dfs(b, i-depth, depth//2)
        
        right=dfs(b, i+depth, depth//2)
        print(i, depth)
        return left and right
                
        
    def check_digit(x, binary_num):
        n=1
        while True:
            if 2**n-1>x:
                binary_num=((2**n-1)-x)*"0"+binary_num
                return binary_num
            if 2**n-1==x:
                return binary_num
            n+=1
    for i in range(len(numbers)):
        if numbers[i]==0:
            answer.append(0)
            continue
        binary_num=bin(numbers[i])[2:]
        binary_num=check_digit(len(binary_num), binary_num)
        result=dfs(binary_num, len(binary_num)//2, (len(binary_num)+1)//4)
        answer.append(1 if result else 0)
    return answer
solution([7, 42, 5])