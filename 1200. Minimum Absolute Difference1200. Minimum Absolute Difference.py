from collections import defaultdict
class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        minDiff=float('inf')
        res=defaultdict(list)

        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]
            res[diff].append([arr[i-1],arr[i]])
            minDiff=min(minDiff,diff)
        return res[minDiff]
