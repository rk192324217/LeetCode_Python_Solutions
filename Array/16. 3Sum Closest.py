class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_diff=float('inf')
        close_sum=float('inf')
        
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1

            while left<right:
                curr_sum=nums[i]+nums[left]+nums[right]
                curr_diff=abs(curr_sum-target)

                if min_diff>curr_diff:
                    min_diff=curr_diff
                    close_sum=curr_sum
                if curr_sum<target:
                    left+=1
                else:
                    right-=1
        return close_sum

