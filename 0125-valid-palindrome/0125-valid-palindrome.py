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
