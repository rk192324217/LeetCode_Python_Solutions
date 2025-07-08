import bisect
class Solution(object):
    def maxValue(self, events, k):
        events.sort(key=lambda event:event[1])
        dp=[[0,0]]
        dp2=[[0,0]]
        for x in range(k):
            for s,e,v in events:
                i=bisect.bisect(dp,[s])-1
                val=dp[i][1]+v
                if val>dp2[-1][1]:
                    dp2.append([e,val])
            dp=dp2
            dp2=[[0,0]]
        return dp[-1][1]

        