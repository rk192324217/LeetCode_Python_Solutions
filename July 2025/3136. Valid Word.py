class Solution(object):
    def isValid(self, word):
               
        if len(word)<3:
            return False
        if not word.isalnum():
            return False

        vowel,const=0,0
        
        for i in word:
            if i in "AEIOUaeiou":
                vowel+=1
            elif i not in "AEIOUaeiou" and i not in "0123456789":
                const+=1

        if vowel>=1 and const>=1:
            return True
        else:
            return False