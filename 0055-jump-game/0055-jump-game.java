class Solution {
    public boolean canJump(int[] nums) {

        int mx_so_far = nums[0]; //Set the mx to first element
        
        for(int i = 1;i<nums.length;i++){
            if(mx_so_far < i){  //if max<i then we cannot reach to end
                return false;
            }
            
            mx_so_far = Math.max(mx_so_far, nums[i]+i);
            
        }
        
         return true;
    }
}