class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=nums[0]
        
        for i in range(1, len(nums)):
            if max_reach<i:
                return False
            else:
                max_reach=max(max_reach, nums[i]+i)
        return True