class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        reverse=[word[::-1] for word in words]
        return ' '.join(reverse)
        