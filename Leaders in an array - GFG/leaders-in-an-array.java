//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.util.stream.*;

class Array {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter ot = new PrintWriter(System.out);
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		
		while(t-->0){
		    
		    //input size of array
		    int n = Integer.parseInt(br.readLine().trim());
		    int arr[] = new int[n];
		    String inputLine[] = br.readLine().trim().split(" ");
		    
		    //inserting elements in the array
		    for(int i=0; i<n; i++){
		        arr[i] = Integer.parseInt(inputLine[i]);
		    }
		    
		    Solution obj = new Solution();
		    
		    StringBuffer str = new StringBuffer();
		    ArrayList<Integer> res = new ArrayList<Integer>();
		  
		    //calling leaders() function
		    res = obj.leaders(arr, n);
		    

		    for(int i=0; i<res.size(); i++){
		        ot.print(res.get(i)+" ");
		    }
		    
		    ot.println();
		}
		ot.close();
		
	}
}

// } Driver Code Ends


class Solution{
    //Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int arr[], int n){
        // Your code here
        ArrayList<Integer> ans= new ArrayList<Integer>();
        int maxElement=arr[n-1];// Assign rightmost element to the maxElement i.e 2
        ans.add(maxElement);//add 2 in the list ans=[2]
        
        for(int i=n-2;i>=0;i--)
        {
            if(arr[i]>=maxElement)// check if arr[i] (starting from 5) is greater than max i.e 2
            {
                ans.add(arr[i]);//if yes then add in the list ans[2, 5]
                maxElement=arr[i]; //max me abb 5 aa jaayega
            }
        }
        Collections.reverse(ans);
        return ans;
    }
}

//{16,17,4,3,5,2}
//1st iteration me 5 greater than hai 2 se to 5 ans me add ho jayega, ans[2,5], maxElement[5]
//2nd iteration me 3 is not greater than 5, to ans me add nhi hoga, ans[2,5], maxElement[5](kyuki poora for loop skip ho ja raha)
//3rd iteration me 4 is not greater than 5, so ans[2,5], maxElement[5]
//4th iteration me 17 is greater than 5, ans[2,5, 17], maxElement[17](kyuki control abb inside the loop hoga)
//5t iteration me 16 is not greater than 17, so ans[2,5,17], maxElement[17]
//now reverse the list ans[17,5,2]
