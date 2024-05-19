class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # nums1[m:]=nums2
        # nums1.sort()
        # return nums1
        # # TC:- O((m+n)log(m+n)), SC:- O(1)
        
        left = m - 1
        right = n - 1
        curr = m + n - 1

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
    
    
        