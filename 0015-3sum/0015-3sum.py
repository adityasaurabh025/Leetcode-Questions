class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        n=len(nums)
        
        
        for i in range(n-2): # run loop till n-2 to get triplets
            if i>0 and nums[i]==nums[i-1]: #check for duplicates
                continue
            left, right=i+1, n-1
        # Now you have fixed the first element and using two pointer approach to compare 2 elements only at a time
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left< right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return res
                    
                
        
            