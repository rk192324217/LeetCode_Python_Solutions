from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        dup,mis=-1,-1
        count=Counter(nums)
        for i in range(1,len(nums)+1):
            if count[i]==2:
                dup=i
            elif count[i]==0:
                mis=i
        return [dup,mis]