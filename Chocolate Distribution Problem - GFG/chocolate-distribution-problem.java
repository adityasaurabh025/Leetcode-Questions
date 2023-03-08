//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main (String[] args)
    {
        
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int n = sc.nextInt();
            ArrayList<Integer> arr = new ArrayList<>();
            for(int i = 0;i<n;i++)
                {
                    int x = sc.nextInt();
                    arr.add(x);
                }
            int m = sc.nextInt();
            
            Solution ob = new Solution();
            
    		System.out.println(ob.findMinDiff(arr,n,m));
        }
        
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{
    public long findMinDiff (ArrayList<Integer> a, int n, int m)
    {
        // your code here
        
        if(n<m) return -1;
        int min=Integer.MAX_VALUE;// consider the initial value as max
        Collections.sort(a); //To sort the ArrayList we use Collections.sort
        for(int i=0;i<=a.size()-m; i++)// i<8-5=3, because last 5 size ka window index 3 tak jayega
        {
            min=Math.min(min,(a.get(i+m-1)-a.get(i)));//min me minimum of difference of end=i+m-1 and start=i
        }
        return (long)min;
        
    }
}

// N = 8, M = 5
// A = {3, 4, 1, 9, 56, 7, 9, 12}

// A=1,3,4,7,9,9,12,56

