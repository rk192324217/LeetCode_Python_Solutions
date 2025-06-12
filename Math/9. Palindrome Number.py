class Solution(object):
    def isPalindrome(self, nums):
        return str(nums)==str(nums)[::-1]
        