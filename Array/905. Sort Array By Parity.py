class Solution(object):
    def sortArrayByParity(self, nums):
        ans1,ans2=[],[]

        for i in nums:
            if i%2==0:
                ans1.append(i)
            else:
                ans2.append(i)
        return ans1+ans2
        