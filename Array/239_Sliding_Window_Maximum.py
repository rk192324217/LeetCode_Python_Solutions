from collections import deque
class Solution:
    def maxSlidingWindow( nums, k):
        #Brute Force Highly in effective 
        # res=[]
        # n=len(nums)
        # for i in range(n-k+1):
        #     maxi=max(nums[i:i+k])
        #     res.append(maxi)
        # return res


        #Efficient way using Deque
        res=[]
        q=deque()
        for i,num in enumerate(nums):
            while q and q[-1]<num:
                q.pop()
            q.append(num)
            if i >=k and nums[i-k]==q[0]:
                q.popleft()
            if i>=k-1:
                res.append(q[0])
        return res
    
#Test Case 1
print(Solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))