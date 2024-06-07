class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # nums1[m:]=nums2
        # nums1.sort()
        # return nums1
        # # TC:- O((m+n)log(m+n)), SC:- O(1)
        
        left = m - 1 # last element of nums1, 3
        right = n - 1 #last element of nums2 , 6
        curr = m + n - 1 #last element of combined array

        # While there are elements in both arrays
        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]: 
                nums1[curr] = nums1[left]
                left -= 1
            else:
                nums1[curr] = nums2[right]
                right -= 1
            curr -= 1

    # If there are remaining elements in nums2, copy them
        while right >= 0:
            nums1[curr] = nums2[right]
            right -= 1
            curr -= 1
        return curr
    
    '''
    Dry Run:
Initialization:
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
left = m - 1 = 2
right = n - 1 = 2
curr = m + n - 1 = 5
Merging Process:
First iteration:

Compare nums1[left] = nums1[2] = 3 and nums2[right] = nums2[2] = 6
Since 3 < 6, set nums1[curr] = nums2[right] = 6
Update right -= 1 and curr -= 1
nums1 = [1, 2, 3, 0, 0, 6]
right = 1, curr = 4
Second iteration:

Compare nums1[left] = nums1[2] = 3 and nums2[right] = nums2[1] = 5
Since 3 < 5, set nums1[curr] = nums2[right] = 5
Update right -= 1 and curr -= 1
nums1 = [1, 2, 3, 0, 5, 6]
right = 0, curr = 3
Third iteration:

Compare nums1[left] = nums1[2] = 3 and nums2[right] = nums2[0] = 2
Since 3 > 2, set nums1[curr] = nums1[left] = 3
Update left -= 1 and curr -= 1
nums1 = [1, 2, 3, 3, 5, 6]
left = 1, curr = 2
Fourth iteration:

Compare nums1[left] = nums1[1] = 2 and nums2[right] = nums2[0] = 2
Since 2 == 2, set nums1[curr] = nums2[right] = 2
Update right -= 1 and curr -= 1
nums1 = [1, 2, 2, 3, 5, 6]
right = -1, curr = 1
At this point, the right index is -1, indicating that all elements from nums2 have been merged. The remaining elements from nums1 (if any) are already in place.
    '''
    
    
        