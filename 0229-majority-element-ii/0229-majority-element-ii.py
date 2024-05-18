class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        result = []
        count = 1
        n = len(nums)
    
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count > n // 3:
                    result.append(nums[i - 1])
                count = 1
    
    # Handle the last element
        if count > n // 3:
            result.append(nums[-1])
    
        return result
            