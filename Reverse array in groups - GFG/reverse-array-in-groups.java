//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

public class GFG {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
        
        //while testcases exist
        while(t-->0){
            
            String inputLine1[] = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine1[0]);
            int k = Integer.parseInt(inputLine1[1]);
            
            ArrayList<Integer> arr = new ArrayList<>();            
            String inputLine2[] = br.readLine().trim().split(" ");
            for(int i=0; i<n; i++){
                arr.add(Integer.parseInt(inputLine2[i]));
            }
            
            Solution obj = new Solution();
            obj.reverseInGroups(arr, n, k);
            
            StringBuffer str = new StringBuffer();
            for(int i=0; i<n; i++){
                str.append(arr.get(i) + " ");
            }
            System.out.println(str);
        }
    }
}


// } Driver Code Ends


//User function Template for Java
class Solution {

   void reverseInGroups(ArrayList<Integer> arr, int n, int k) {

          ArrayList<Integer> al  = new ArrayList<>();//create an arraylist to add all the elements

        for(int i =0; i<n; i= i+k){// run the loop by k times in each iteration

           int start = i;

           int end= Math.min(n-1,i+k-1);//i+k isliye liye hain kyuki each iteration i+k times increase
           //ho rahe, so i+k-1 hamesha next subgroup ke ek element pehle rahega
           //{1,2,3,4,5}
           //start=1
           //end=4
           //start=2
           //end

           while(end>start){

               Collections.swap(arr,end,start);

               end--;

               start++;

           }

           }

    }

}

//write a func reverse till k
//call the function till k and add in the list


