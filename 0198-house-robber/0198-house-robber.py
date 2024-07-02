class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        elif len(nums)==0:
            return [0]
        
        prev1 = 0
        prev2 = 0

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        return prev1
                