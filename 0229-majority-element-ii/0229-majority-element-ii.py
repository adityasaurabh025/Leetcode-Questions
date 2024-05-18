class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp={}
        res=[]
        n=len(nums)
        
        for num in nums:
            if num in mp:
                mp[num]+=1
                #If num is already a key in mp, this line increments the count (value) associated with num by 1. This means num has been seen again in the list.
            else:
                mp[num]=1
                #If num is not already a key in count_map, this block executes. It adds num as a new key to count_map with a value of 1, indicating that num has been seen for the first time.
        for num, count in mp.items():
            if count > n // 3:
                res.append(num)
    
        return res
    
#         if not nums:
#             return []

#         nums.sort()
#         result = []
#         count = 1
#         n = len(nums)
    
#         for i in range(1, n):
#             if nums[i] == nums[i - 1]:
#                 count += 1
#             else:
#                 if count > n // 3:
#                     result.append(nums[i - 1])
#                 count=1
    
#     # Handle the last element
#         if count > n // 3:
#             result.append(nums[-1])
    
#         return result
            
            