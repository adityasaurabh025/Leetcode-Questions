class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        
        for num in nums:
            if num in seen:
                return True
                
            seen.add(num)
        return False
        
            #return len(nums) > len(set(nums))
        #TC:- O(N), SC:- O(N)

#Algo
''' 
Sort the list
iterate through the list
If first element is equal to second - then it has twice elements
return true
else
return false

Demerits:-
we will have to iterate through all the list if it has very large number

so, convert the list into set and 
'''
 
#         sorted_list= nums.sort()
#         length=len(nums)
#         for num in range(length-1):
#             if nums[num]==nums[num+1]:
#                 return True
#         return False
# TC:- O(nlogn), SC:- O(1)


        
        
        
         