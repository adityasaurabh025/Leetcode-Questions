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

            
            
            
        