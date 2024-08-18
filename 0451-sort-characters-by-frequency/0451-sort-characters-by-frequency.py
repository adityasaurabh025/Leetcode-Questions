from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
    
    # Step 2: Build a max-heap using negative frequencies
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(max_heap)
    
    # Step 3: Construct the result string
        result = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char * -freq)  # Multiply character by its frequency
    
        return ''.join(result)
        
        
        
        
        
        
        
        
        
        """
        words_count= Counter(s)
        
        sorted_chars= sorted(words_count.items(), key= lambda x:(-x[-1], x[0]))
        
        res=''.join(char* freq for char, freq in sorted_chars)
        
        return res
        
        TC- O(nlogn)
        
        Counting Frequencies:

char_count = Counter(s) creates a Counter object that maps each character to its frequency.
Sorting by Frequency:

sorted(char_count.items(), key=lambda x: (-x[1], x[0])) sorts the list of (character, frequency) tuples first by frequency in descending order (-x[1]) and then by character in ascending order (x[0]) as a tiebreaker if necessary.
Building the Result:

''.join(char * freq for char, freq in sorted_chars) constructs the resulting string by repeating each character according to its frequency and concatenating them.
        """
        
        
        
        