class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]: ##If both slow and fast are equal, it means a duplicate element is found, so the fast pointer is incremented to move to the next element.
                fast += 1
            else:
                nums[slow+1] = nums[fast] ##If the elements are not equal, it means a unique element is found. In this case, the next position after slow is updated with the value of the element at index fast.
                #Then both pointers, fast and slow, are incremented by 1 to move to the next elements.
                fast += 1
                slow += 1

        return slow + 1 #Finally, the function returns slow + 1, which represents the length of the resulting list without duplicates.
    
    
"""
The slow pointer represents the last unique element found so far, and the fast pointer represents the current element being checked.

"""