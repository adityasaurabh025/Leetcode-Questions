class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i=0
        cookies_i=0
        
        while child_i< len(g) and cookies_i< len(s):
            if s[cookies_i]>= g[child_i]:
                child_i+=1
            cookies_i+=1
            
        return child_i
        
        """
        The sorting-based approach is already quite efficient with a time complexity of 
\U0001d442
(
\U0001d45b
log
⁡
\U0001d45b
+
\U0001d45a
log
⁡
\U0001d45a
)
O(nlogn+mlogm). However, if sorting is not allowed or if you are looking for further optimization, there are alternative approaches that you can consider, although they typically don't offer a significant improvement over sorting in practical scenarios.

Here’s an alternative approach using counting sort for a constrained input space:

Counting Sort-Based Approach
If the maximum value of the greed factors and the sizes of the cookies is known and bounded, you can use counting sort to sort the arrays. This approach can be more efficient than comparison-based sorting algorithms like quicksort or mergesort for certain types of data.

Time Complexity
Counting sort works in 
\U0001d442
(
\U0001d45b
+
\U0001d45a
+
\U0001d458
)
O(n+m+k) where 
\U0001d458
k is the range of the input values.
This can be faster than 
\U0001d442
(
\U0001d45b
log
⁡
\U0001d45b
+
\U0001d45a
log
⁡
\U0001d45a
)
O(nlogn+mlogm) when 
\U0001d458
k is small relative to 
\U0001d45b
n and 
\U0001d45a
m.
        """
        
        
        