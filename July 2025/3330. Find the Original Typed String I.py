class Solution(object):
    def possibleStringCount(self, word):
        if not word:
            return 0
        ans=1
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                ans+=1
        return ans