class Solution {
    public int arraySign(int[] nums) {
        
        
        int cnt=0; //initialize cnt to count the number of negative integers 
        
        for(int num: nums) //iterate on array to check for negative numbers
        {
            if(num==0) return 0;
            if(num<0) cnt++; //if we find any negative number then increase the count 
        }
        return cnt%2==0 ? 1: -1; //if count of negative number is even that means final
        //output will be positive - - =+, if it is not even then we return -1 for odd number of integers.
        
        //TC- O(n) for traversing through n arrays terms
        
        
    }
}