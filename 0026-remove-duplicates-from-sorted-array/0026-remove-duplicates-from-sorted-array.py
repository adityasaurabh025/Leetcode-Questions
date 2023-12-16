class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:] = list(set(nums)) #nums[:] is known as list slicing, and it refers to the entire list nums. The [:] slice notation essentially creates a copy of the entire list.
        # nums.sort()
        # return len(nums)
        
        if not nums:
            return 0

        k = 1  # Pointer to track the position of unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # If current element is different from previous
                nums[k] = nums[i]  # Move the unique element to the correct position
                k += 1  # Increment the pointer

        return k