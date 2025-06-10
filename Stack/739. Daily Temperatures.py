class Solution(object):
    def dailyTemperatures(self, temperatures):
        length=len(temperatures)
        res=[0]*length
        stack=[]
        
        for i in range(length):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx=stack.pop()
                res[idx]+=i-idx
            stack.append(i)
        return res
        


        