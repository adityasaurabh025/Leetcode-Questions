import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return s == s[::-1]
    
    """
    
    class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize pointers
        left, right = 0, len(s) - 1
        
        # Iterate until pointers meet or cross
        while left < right:
            # Skip non-alphanumeric characters
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            # Convert characters to lowercase for comparison
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        # If the loop completes, it's a palindrome
        return True

    re.sub(): This function is from the re module in Python and is used for performing substitution in strings using regular expressions.
r'[^a-zA-Z0-9]': This is the regular expression pattern used to match any character that is not an alphanumeric character. Here's what each part of the pattern means:
[^...]: This is a negated character class, which matches any character not contained within the square brackets.
a-zA-Z0-9: This matches any alphanumeric character (either lowercase letter, uppercase letter, or digit). The hyphen - denotes a range of characters from a to z, A to Z, and 0 to 9.
'': This is the replacement string, which is empty in this case. This means that any non-alphanumeric characters matched by the pattern will be replaced with nothing, effectively removed from the string.
    """