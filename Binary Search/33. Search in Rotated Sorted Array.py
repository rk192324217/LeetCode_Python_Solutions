class Solution:
    def search(self, nums, target) :
        f , l = 0 , len(nums)-1
        while f<=l:
            mid=(l+f)//2
            if nums[mid]==target:
                return mid
            if nums[f]<=nums[mid]:
                if nums[f]<=target<nums[mid]:
                    l=mid-1
                else:
                    f=mid+1
            else:
                if nums[mid]<target <=nums[l]:
                    f=mid+1
                else:
                    l=mid-1
        return -1       