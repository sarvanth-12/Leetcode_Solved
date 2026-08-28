class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in range(len(digits)):
            s+=str(digits[i])
        su=int(s)+1
        di=list(map(int,str(su)))
        return di
            

        