class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()
        reverse_word= words[::-1]
        
        reverseString= ' '. join(reverse_word)
        return reverseString
        
        
    
    """
    Approach 1:
    Split into list, reverse and return O(nlogn)
    
    create an extra array, place the elements of original array into new array by
    substracting with total number of arrays
    
    """