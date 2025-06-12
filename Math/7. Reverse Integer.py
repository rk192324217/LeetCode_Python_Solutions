class Solution(object):
    def reverse(self, x):
        ans=int(str(abs(x))[::-1])
        if x<0:
            ans=-ans
        if ans< -2**31 or ans > 2**31-1:
            return 0
        return ans
        