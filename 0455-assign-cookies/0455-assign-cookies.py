class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i=0
        cookies_i=0
        
        while child_i< len(g) and cookies_i< len(s):
            if s[cookies_i]>= g[child_i]:
                child_i+=1
            cookies_i+=1
            
        return child_i
        
        
        
        