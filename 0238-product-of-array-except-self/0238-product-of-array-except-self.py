class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Approach:-
        ->create extra Array.
        ->Loop through array.
        ->take product of all the j elements untill i==j(because i should not be included)
        -> Add in ans array and return
        TC:- O(n^2)
        SC:- O(N)
        
        Demerits: It will not pass testcases for large inputs, will throw TLE
        ans = []
        for i in range(len(nums)):
            prd = 1
            for j in range(len(nums)):
                if i != j:
                    prd *= nums[j]
            ans.append(prd)
        return ans
        
        Approach 2:
        -> Create extra array
        -> Loop through array and take products of all elements
        -> Loop through array again and divide each element with nums[i]
        -> return and
        TC: O(N)
        SC:- O(N)
        Demerits: You cannot divide 0, so testcases will fail
        ans=[]
        prd=1
        for i in range(len(nums)):
            prd*=nums[i]
        for i in range(len(nums)):
            ans.append(prd//nums[i])
        return ans
        '''
        n=len(nums)
        pre=[1]*n
        suff=[1]*n
        ans=[0]*n
        
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        # Calculate final products using prefix and suffix products
       
        for i in range(n):
            ans[i]=(pre[i] * suff[i])
        return ans
        
        
        