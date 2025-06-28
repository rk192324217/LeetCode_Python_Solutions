class Solution(object):
    def backspaceCompare(self, s, t):
        def check(string):
            st=[]
            for i in string:
                if st and i == '#' :
                    st.pop()
                elif not st and i=="#":
                    continue
                else:
                    st.append(i)
            return st

        return check(s)==check(t)        