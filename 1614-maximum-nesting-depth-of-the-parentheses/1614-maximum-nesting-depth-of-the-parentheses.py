from collections import Counter

class Solution:
    def maxDepth(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s)==1 and s!=')' and s!='(':
            return 0
        
        else:
            par1=0
            par2=0
            splitted_chars=list(s)
            for chars in splitted_chars:
                if chars=='(':
                    par1+=1
                elif chars==')' and par1>0:
                    par2= max(par1, par2)
                    par1-=1
        return par2