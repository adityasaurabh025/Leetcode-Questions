class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        sumOfAll= (n*(n+1)//2)
        sumOfArr= sum(nums)
        result= sumOfAll - sumOfArr
        return result