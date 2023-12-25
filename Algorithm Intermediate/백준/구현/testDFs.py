n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

a = []

def dfs(L):
    if len(a)==m:
        print(*a)
        return
    tmp = 0
    for i in range(L, n):
       if tmp != nums[i]:
           a.append(nums[i])
           tmp=nums[i]
           dfs(i)
           a.pop()
       

dfs(0)