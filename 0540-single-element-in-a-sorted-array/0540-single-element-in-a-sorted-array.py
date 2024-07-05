class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            mid = (low + high) // 2

        # Check if mid is even or odd to determine the pair check
            if mid % 2 == 0:
                if arr[mid] == arr[mid + 1]:
                    low = mid + 2
                else:
                    high = mid
            else:
                if arr[mid] == arr[mid - 1]:
                    low = mid + 1
                else:
                    high = mid

        return arr[low]
        
        
        
        
        
        
#         freq={}
        
#         for num in nums:
#             if num in freq:
#                 freq[num]+=1
#             else:
#                 freq[num]=1
        
#         for num in nums:
#             if freq[num]==1:
#                 return num
#         return -1
#         TC:- O(N), SC- O(N)

"""
Mid Calculation:

First iteration: mid = (0 + 8) // 2 = 4.

mid is even.

Check nums[mid] (3) and nums[mid + 1] (4).

If nums[mid] is equal to nums[mid + 1], it means the unpaired element is in the right half (not the case here).

Since nums[mid] (3) is not equal to nums[mid + 1] (4), the single element is in the left half. Set high = mid = 4.

Next Iteration:

Now, low = 0, high = 4.

Calculate mid = (0 + 4) // 2 = 2.

mid is even.

Check nums[mid] (2) and nums[mid + 1] (3).

If nums[mid] is equal to nums[mid + 1], it means the unpaired element is in the right half (not the case here).

Since nums[mid] (2) is not equal to nums[mid + 1] (3), the single element is in the left half. Set high = mid = 2.

Final Iteration:

Now, low = 0, high = 2.

Calculate mid = (0 + 2) // 2 = 1.

mid is odd.

Check nums[mid] (1) and nums[mid - 1] (1).

If nums[mid] is equal to nums[mid - 1], it means the unpaired element is in the right half (true in this case).

Since nums[mid] (1) is equal to nums[mid - 1] (1), the single element is in the right half. Set low = mid + 1 = 2.

Now, low = 2 and high = 2. Thus, the loop exits, and the single element is nums[low], which is 2.

Summary of the Algorithm
Even mid:
If nums[mid] == nums[mid + 1], the single element is in the right half.
Else, the single element is in the left half.
Odd mid:
If nums[mid] == nums[mid - 1], the single element is in the right half.
Else, the single element is in the left half.
"""
            
            
            
        