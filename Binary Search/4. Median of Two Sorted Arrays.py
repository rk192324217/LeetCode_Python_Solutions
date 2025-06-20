class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_arr=sorted(nums1+nums2)
        l,r=0,len(merged_arr)
        center=(l+r)//2
        median=0
        if r%2==0:
            median=(merged_arr[center-1]+merged_arr[center])/2.0
        else:
            median=merged_arr[center]*1.0
        return median