class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1




        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1