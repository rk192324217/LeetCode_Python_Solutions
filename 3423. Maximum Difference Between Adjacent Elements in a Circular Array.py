class Solution(object):
    def maxAdjacentDistance(self, nums):
        n=len(nums)
        max_diff=0
        for i in range(1,n):
            diff=abs(nums[i]-nums[i-1])
            if diff>max_diff:
                max_diff=diff

        diff=abs(nums[n-1]-nums[0])
        if diff>max_diff:
            return diff
        else:        
            return max_diff