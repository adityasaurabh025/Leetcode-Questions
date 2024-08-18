class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={}
        stack=[]
        
        for num in nums2:
            while stack and num> stack[-1]:
                next_greater[stack.pop()]= num
            stack.append(num)
        while stack:
            next_greater[stack.pop()]=-1
        ans= [next_greater[num] for num in nums1]
        
        return ans
        
        """
        ans=[-1]*len(nums1)
        
        for i in range(len(nums1)):
            num= nums1[i]
            index_in_nums2 = nums2.index(num)
            next_greater=-1
            
            for j in range(index_in_nums2+1, len(nums2)):
                if nums2[j]> num:
                    next_greater= nums2[j]
                    break
            ans[i]= next_greater
        return ans
        
        TC- O(M*N), SC:- O(M)
                    
        """