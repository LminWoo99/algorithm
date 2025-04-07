class Solution(object):
    def minimumPairRemoval(self, nums):
        res=0
        while sorted(nums)!=nums:
            tmp=int(1e9)
            x=1
            for i in range(2, len(nums)):
                if nums[i]+nums[i-1]<nums[x]+nums[x-1]:
                    x=i
            new_num=[]
            for i in range(len(nums)):
                if i==x:
                    continue
                if i+1==x:
                    new_num.append(nums[i]+nums[i+1])
                else:
                    new_num.append(nums[i])
            nums=new_num[:]
            
            res+=1
        return res       
                
            
            
        """
        :type nums: List[int]
        :rtype: int
        """
        