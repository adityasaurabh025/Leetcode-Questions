import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        # Check if the string is a palindrome
        return s == s[::-1]
    
    """
    re.sub(): This function is from the re module in Python and is used for performing substitution in strings using regular expressions.
r'[^a-zA-Z0-9]': This is the regular expression pattern used to match any character that is not an alphanumeric character. Here's what each part of the pattern means:
[^...]: This is a negated character class, which matches any character not contained within the square brackets.
a-zA-Z0-9: This matches any alphanumeric character (either lowercase letter, uppercase letter, or digit). The hyphen - denotes a range of characters from a to z, A to Z, and 0 to 9.
'': This is the replacement string, which is empty in this case. This means that any non-alphanumeric characters matched by the pattern will be replaced with nothing, effectively removed from the string.
    """