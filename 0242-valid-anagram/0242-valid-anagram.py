class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t) 
        
        

'''
convert string to chars

Approach 2:
Dictionary

convert each chars into dict and keep the count of each chars
If count of each chars of s is matching with count of each chars of t
return true
'''