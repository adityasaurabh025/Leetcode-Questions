class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        arr.sort()
        count=0
        majority=(len(arr)//2)
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=1
                if count>majority:
                    return arr[i]
            else:
                count=1
        return arr[0]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      #sort and count
      #dict se count
        
        