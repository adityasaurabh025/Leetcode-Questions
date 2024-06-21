class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high= n-1
        
        while low<= high:
            mid= (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                high= mid-1
            else:
                low= mid+1
                
        return low
    
    """
    Why Return low?
If during the binary search loop, target is found (target == nums[mid]), we return mid.
If target is not found and we exit the loop (low > high), it means low has crossed high, indicating the position where target should be inserted:
Insertion Logic: low represents the index where target should be placed without violating the sorted order of nums.
Why low?: After the last iteration of the loop, low will always point to the position where target should be inserted:
If target is greater than all elements in nums, low will be len(nums), which is the correct insertion position.
If target should be inserted before the first element or somewhere in between, low will indicate the correct index.
    """
        