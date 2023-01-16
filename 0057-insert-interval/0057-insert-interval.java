// This code defines a class Solution that contains a method insert which takes in two parameters: an array of intervals represented by a 2D array, and a new interval represented by a 1D array. The method returns a new 2D array containing the merged intervals.

// The approach of this code is to add the intervals that come before the new interval to the answer arraylist, then check if the new interval should be merged with the last interval in the answer arraylist, and finally, add the remaining intervals from the input array to the answer arraylist.

// The code first initializes an empty ArrayList called ans. The variable idx is initialized to 0, and the while loop iterates through the input intervals array. The loop compares the starting value of the current interval with the starting value of the new interval, and if the current interval's starting value is less than the new interval's starting value, it is added to the ans arraylist. If the starting value of the current interval is greater than or equal to the new interval's starting value, the loop breaks. This ensures that the intervals in the ans arraylist will be in the same order as they were in the input array, but with the new interval inserted in the correct position.

// Next, the code checks if the ans arraylist is empty or if the new interval's starting value is greater than the last interval's ending value in the ans arraylist. If either of these conditions is true, the new interval is added to the ans arraylist. Otherwise, the last interval in the ans arraylist is merged with the new interval by updating the last interval's ending value to be the maximum of the last interval's ending value and the new interval's ending value.

// Finally, the while loop iterates through the remaining intervals in the input array. The loop compares the ending value of the last interval in the ans arraylist with the starting value of the current interval. If the last interval's ending value is greater than or equal to the current interval's starting value, it means the two intervals overlap and should be merged. The last interval's ending value is updated to be the maximum of the last interval's ending value and the current interval's ending value. If the last interval's ending value is less than the current interval's starting value, it means the two intervals do not overlap and the current interval is added to the ans arraylist.

// After the while loop, the ans arraylist is converted to a 2D array and returned as the final output.

//TC = O(n)
//Sc = O(n)
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {   
       // Initialize an ArrayList to hold the merged intervals
        ArrayList<int[]> ans = new ArrayList<>();
        // Initialize a variable to track our position in the input intervals array
        int idx = 0;
        // Loop through the input intervals
        while(idx < intervals.length){
            // If the current interval starts before the new interval, add it to the answer list
            if(intervals[idx][0] < newInterval[0]){
                ans.add(intervals[idx]);
                idx++;
            // If the current interval starts after or at the same time as the new interval, exit the loop
            }else{
                break;
            }
        }
        // If the answer list is empty or the last interval in the answer list ends before the new interval starts
        // add the new interval to the answer list
        if(ans.size() == 0 || (newInterval[0] > ans.get(ans.size()-1)[1])){
            ans.add(newInterval);
        // If the last interval in the answer list overlaps with the new interval, merge them by updating the end time of the last interval
        }else{
            int[] lastInterval = ans.get(ans.size()-1);
            lastInterval[1] = Math.max(lastInterval[1],newInterval[1]);
        }
        // Loop through the remaining intervals in the input array
        while(idx < intervals.length){
            int[] lastInterval = ans.get(ans.size()-1);
            // If the last interval in the answer list overlaps with the current interval, merge them by updating the end time of the last interval
            if(lastInterval[1] >= intervals[idx][0]){
                lastInterval[1] = Math.max(lastInterval[1], intervals[idx][1]);
            }else{
                // If the last interval does not overlap with the current interval, add it to the answer list
                ans.add(intervals[idx]);
            }
            idx++;
        }
        // Convert the ArrayList to a 2D int array and return it
        return ans.toArray(new int[ans.size()][]);
    }
}

