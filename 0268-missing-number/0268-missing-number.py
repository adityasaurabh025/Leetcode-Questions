class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        # sumOfAll= (n*(n+1)//2)
        # sumOfArr= sum(nums)
        # result= sumOfAll - sumOfArr
        # return result
        xor =0
        
        for i in range(n):
            xor^=nums[i]
        for i in range(1,n+1):
            xor^=i
        return xor
    """
    When we XOR all the numbers in the nums list, any number that appears twice will cancel out, leaving only the missing number.
Similarly, when we XOR all the numbers from 1 to n, any number that appears twice will cancel out, leaving only the missing number.
Finally, XORing the two results will leave us with only the missing number, as the other numbers will have been XORed twice and canceled out.
    """