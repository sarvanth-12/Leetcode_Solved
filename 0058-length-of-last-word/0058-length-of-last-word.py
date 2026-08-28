class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.split()
        p=" ".join(s)
        res=p.split()
        f=res[len(res)-1]
        return len(f)
        

            
                
        