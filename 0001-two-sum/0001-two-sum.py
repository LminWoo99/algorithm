class Solution(object):
    def twoSum(self, nums, target):
        res=[0,0]
        tmp=[[0]*2 for _ in range(len(nums))]
        for idx, val in enumerate(nums):
            tmp[idx][0]=val
            tmp[idx][1]=idx
        tmp.sort()
        for i in range(len(tmp)-1):
            start,end=i, len(tmp)-1
            flag=False
            while start<end:
                mid=tmp[start][0]+tmp[end][0]
                if mid==target:
                    flag=True
                    res[0]=tmp[start][1]
                    res[1]=tmp[end][1]
                    break
                if mid>target:
                    end-=1
                else:
                    start+=1
            if flag:
                break
        return res