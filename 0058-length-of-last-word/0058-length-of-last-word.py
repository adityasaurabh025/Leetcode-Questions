class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited= s.split()
        return len(splited[-1])