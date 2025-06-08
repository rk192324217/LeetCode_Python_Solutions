class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        uniqueset=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                k=j+1
                l=n-1
                while k<l:
                    targetSum=nums[i]+nums[j]+nums[k]+nums[l]
                    if targetSum==target:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        uniqueset.add(tuple(temp))
                        k+=1
                        l-=1
                    elif targetSum<target:
                        k+=1
                    elif targetSum>target:
                        l-=1
        return list(uniqueset)