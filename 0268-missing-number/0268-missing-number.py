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