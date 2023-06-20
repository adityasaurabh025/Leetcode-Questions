class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k 
        