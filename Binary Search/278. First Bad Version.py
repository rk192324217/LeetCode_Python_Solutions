# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        l,r=1,n
        while l<r:
            mid=l+(r-l)//2
            if isBadVersion(mid): # type: ignore
                r=mid
            else:
                l=mid+1
        return l        