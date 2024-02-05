class Solution:
    def expand_from_center(left, right):
        """
        Algorithm :
At starting we have maz_str = s[0] and max_len = 1 as every single character is a palindrome.
Now, we will iterate over the string and for every character we will expand around its center.
For odd length palindrome, we will consider the current character as the center and expand around it.
For even length palindrome, we will consider the current character and the next character as the center and expand around it.
We will keep track of the maximum length and the maximum substring.
Print the maximum substring.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
    
        # maxLen=0 # max Length of string
        # maxStr=s[0] #max String found so far
        
#         for i in range(len(s)-1): 
#             for j in range(i+1, len(s)):
#                 if j-i+1> maxLen and s[i:j+1]==s[i:j+1][::-1]:
#                     #check max length and reverse of that length if both condition satisfies then palindrome found
#                     maxLen= j-i+1
#                     maxStr= s[i:j+1]
                    
#         return maxStr
#     # TC:O(n*3), TC:-O(1)


    
    