"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k
        
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-2,0,-1): # Running loop from last -2 element to 0 and decrement -1 each time
            if(nums[i]==nums[i-1] and nums[i]==nums[i+1]): # if next and previous element of the current index is equal that means duplicates are there
                nums.pop(i-1) #pop the element that is duplicate either from next or prevoius index
        return len(nums)
       