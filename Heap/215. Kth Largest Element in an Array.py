class Solution(object):
    def findKthLargest(self, nums, k):
        nums=sorted(nums)
        return nums[len(nums)-k]
        