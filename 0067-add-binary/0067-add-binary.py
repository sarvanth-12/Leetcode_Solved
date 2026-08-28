class Solution(object):
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        s=a+b
        q=bin(s)[2:]
        return q