class Solution:
    def containsDuplicate(self, nums):
        return not len(nums)==len(set(nums))