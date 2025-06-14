class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key= lambda x : x[1])
        count=0
        n=len(intervals)
        end=float('-inf')
        for i in intervals:
            if i[0]>=end:
                end=i[1]
            else:
                count+=1
        return count