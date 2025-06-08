class Solution(object):
    def twoSum(self, numbers, target):
        if not numbers:
            return []
        i,j=0,len(numbers)-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s==target:
                return [i+1,j+1]
            elif s<target:
                i+=1
            else:
                j-=1
        
sol=Solution()
numbers = [2,7,11,15]
target = 9
result=sol.twoSum(numbers,target)
print(result)