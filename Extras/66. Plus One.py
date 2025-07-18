class Solution(object):
    def plusOne(self, digits):
        st=""
        for i in digits:
            st+=str(i)
        
        num=int(st)+1
        res=[]
        for i in str(num):
            res.append(int(i))

        return res
