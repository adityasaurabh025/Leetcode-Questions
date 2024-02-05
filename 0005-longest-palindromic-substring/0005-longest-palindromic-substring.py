class Solution:
    def expand_from_center(left, right):
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


    
    