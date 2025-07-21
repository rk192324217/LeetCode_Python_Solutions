class Solution(object):
    def makeFancyString(self, s):
        res=[]
        for i in s:
            if len(res)>=2 and res[-1]==i and res[-2]==i:
                continue
            res.append(i)
        return "".join(res)
        