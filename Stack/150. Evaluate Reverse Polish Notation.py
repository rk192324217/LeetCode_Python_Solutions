class Solution(object):
    def evalRPN(self, tokens):
        stck=[]
        for i in tokens:
            if i == "+":
                stck.append(stck.pop()+stck.pop())
            elif i == "-":
                s,f=stck.pop(),stck.pop()
                stck.append(f-s)
            elif i == "*":
                stck.append(stck.pop() * stck.pop())
            elif i == "/":
                s,f=stck.pop(),stck.pop()
                stck.append(int(float(f)/s))
            else:
                stck.append(int(i))
        return stck[0]
        