class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        k=[]
        for i in nums:
            if i%2==0:
                k.append(i)
        sum=0
        for i in range(0,len(k)):
            sum=sum|k[i]
        return sum
        