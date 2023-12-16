class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums)) #nums[:] is known as list slicing, and it refers to the entire list nums. The [:] slice notation essentially creates a copy of the entire list.
        nums.sort()
        return len(nums)