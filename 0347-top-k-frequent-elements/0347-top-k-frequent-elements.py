class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = Counter(nums)
    
    # Sort the dictionary items by frequency in descending order
        sorted_by_frequency = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Get the k most frequent elements
        if k <= len(sorted_by_frequency):
            return [element for element, _ in sorted_by_frequency[:k]]
        else:
            return None  