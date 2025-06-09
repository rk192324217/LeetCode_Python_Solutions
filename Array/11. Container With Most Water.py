class Solution(object):
    def maxArea(self, height):
        left,right=0,len(height)-1
        maxi=0
        while left<right:
            h=min(height[left],height[right])
            w=right-left
            area=h*w
            maxi=max(maxi,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi