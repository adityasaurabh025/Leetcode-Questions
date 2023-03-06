//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        
        while(t-- > 0)
        {
            String str[] = read.readLine().trim().split(" ");
            int n = Integer.parseInt(str[0]);
            
            int arr[] = new int[n];
            int dep[] = new int[n];
            
            str = read.readLine().trim().split(" ");
            for(int i = 0; i < n; i++)
              arr[i] = Integer.parseInt(str[i]);
            str = read.readLine().trim().split(" ");
            for(int i = 0; i < n; i++)
                dep[i] = Integer.parseInt(str[i]);
                
            System.out.println(new Solution().findPlatform(arr, dep, n));
        }
    }
    
    
}



// } Driver Code Ends


//User function Template for Java

class Solution
{
    //Function to find the minimum number of platforms required at the
    //railway station such that no train waits.
    static int findPlatform(int arr[], int dep[], int n)
    {
        // add your code here
        //1st approach, using nested loop
        //*************************************************************
        // int plat_needed = 1, result = 1;
 
        // // run a nested  loop to find overlap
        // for (int i = 0; i < n; i++) {
        //     // minimum platform
        //     plat_needed = 1;
 
        //     for (int j = 0; j < n; j++) {
        //         if (i != j)
        //             // check for overlap
        //             if (arr[i] >= arr[j]
        //                 && dep[j] >= arr[i])
        //                 plat_needed++;
        //     }
 
        //     // update result
        //     result = Math.max(result, plat_needed);
        // }
 
        // return result;
        //TC-O(N^2)
        //*******************************************************************
        
        //SORTING APPROACH
        // arr = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
        // dep = [9:10, 11:20, 11:30, 12:00, 19:00, 20:00]
        Arrays.sort(arr);
        Arrays.sort(dep);
 
        // plat_needed indicates number of platforms
        // needed at a time
        int plat_needed = 1, result = 1;
        int i = 1, j = 0;
 
        // Similar to merge in merge sort to process
        // all events in sorted order
        while (i < n && j < n) {
            // If next event in sorted order is arrival,
            // increment count of platforms needed
            if (arr[i] <= dep[j]) {
                plat_needed++;
                i++;
            }
 
            // Else decrement count of platforms needed
            else if (arr[i] > dep[j]) {
                plat_needed--;
                j++;
            }
 
            // Update result if needed
            if (plat_needed > result)
                result = plat_needed;
        }
 
        return result;
    }
    
}

//if any trains comes between arr and dep time of one train, then cnt++
//Heaps take log(n) time for pushing element and there are n elements.
// https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

 