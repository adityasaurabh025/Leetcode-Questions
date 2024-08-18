from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        words_count= Counter(s)
        
        sorted_chars= sorted(words_count.items(), key= lambda x:(-x[-1], x[0]))
        
        res=''.join(char* freq for char, freq in sorted_chars)
        
        return res
        
        
        
        
        