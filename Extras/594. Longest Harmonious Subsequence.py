class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        j,maxlen=0,0
        for i in range(len(nums)):
            while nums[i]-nums[j]>1:
                j+=1
            if nums[i]-nums[j]==1:
                maxlen=max(maxlen,i-j+1)
        return maxlen