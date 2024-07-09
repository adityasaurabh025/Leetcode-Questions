class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i]<=k:
                k+=1
            else:
                break
        return k
    
    """
    Incrementing k Based on Array Elements:

The loop iterates through each element arr[i] in the array arr.
If arr[i] <= k, it means that arr[i] is a number that exists in the sequence up to k (or possibly the next missing number).
Therefore, k is incremented by 1 (k += 1).
Breaking the Loop:

As soon as an element arr[i] is encountered that is greater than k, the loop breaks (break statement).
This indicates that arr[i] is the first number encountered in arr that is greater than k, meaning k has reached or surpassed the count of positive integers up to the kth missing positive integer.
Returning k:

After exiting the loop, the current value of k is returned.
This value of k represents the count of positive integers (including the missing ones) up to the kth missing positive integer from arr.
    """