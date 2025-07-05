from collections import Counter
class Solution:
    def findLucky(self, arr):
        count=Counter(arr)
        n=max(arr)
        lucky=-1
        for i in range(1,n+1):
            if count[i]==i:
                lucky=max(lucky,i)
        return lucky