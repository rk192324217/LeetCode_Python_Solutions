class Solution(object):
    def divideString(self, s, k, fill):
        req=len(s)%k
        res=[]
        if req==0:
            for i in range(0,len(s),k):
                res.append(s[i:i+k])
        else:
            s+=fill*(k-req)
            for i in range(0,len(s),k):
                res.append(s[i:i+k])
        
        return res