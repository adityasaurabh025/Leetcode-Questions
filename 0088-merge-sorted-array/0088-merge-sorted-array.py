class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # nums1[m:]=nums2
        # nums1.sort()
        # return nums1
        # # TC:- O((m+n)log(m+n)), SC:- O(1)
        
        left = m - 1 # last element of nums1
        right = n - 1 #last element of nums2
        curr = m + n - 1 #last element of combined array

        # While there are elements in both arrays
        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]: 
                #0>6, which is false, loop will go to else block
                #0>5, which is false, loop will go in else block
                #0>2, which is false, loop will go in else block
                #3>2, true, below code will execute, []
                nums1[curr] = nums1[left]
                left -= 1
            else:
                nums1[curr] = nums2[right]
                #In first iteration, [0,0,0,0,0,6]
                #In second iteration, [0,0,0,0,5,6]
                #In third iteration, [0,0,0,2,5,6]
                right -= 1
            curr -= 1

    # If there are remaining elements in nums2, copy them
        while right >= 0:
            nums1[curr] = nums2[right]
            right -= 1
            curr -= 1
        return curr
    
    
        