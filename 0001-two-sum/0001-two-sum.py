class Solution:
    def twoSum(self, nums, target):
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = sorted_nums[left][1] + sorted_nums[right][1]
            if curr_sum == target:
                return [sorted_nums[left][0], sorted_nums[right][0]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return []
        
        
        


