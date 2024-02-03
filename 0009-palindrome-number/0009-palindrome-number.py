class Solution:
    def isPalindrome(self, x: int) -> bool:
        rem=0
        if x>=0:
            temp=x
            rev_sum=0
            while x>0:
                rem=x%10
                rev_sum=(rev_sum*10)+rem
                x//=10
            if rev_sum==temp:
                return True
            else:
                return False
                
        else:
            return False
        