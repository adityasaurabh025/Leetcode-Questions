class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t) 
        if(len(s)!=len(t)):
            return False
        s_count={}
        t_count={}
        
        for char in s:
            s_count[char]=s_count.get(char, 0)+1
            
        for char in t:
            t_count[char]=t_count.get(char, 0)+1
        
        return s_count==t_count
        

'''
convert string to chars

Approach 2:
Dictionary

convert each chars into dict and keep the count of each chars
If count of each chars of s is matching with count of each chars of t
return true
'''