class MinStack(object):

    def __init__(self):
        self.st=[]

    def push(self, val):
        minval=self.getMin()
        if minval==None or val<minval:
            minval=val
        self.st.append([val,minval])

    def pop(self):
        self.st.pop()

    def top(self):
        return self.st[-1][0]

    def getMin(self):
        return self.st[-1][1] if self.st else None
