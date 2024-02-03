class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                return False

        return not stack
    
    """
    Loop through each character in the string (for char in s):

The code iterates through each character in the input string s.
Check if the character is an open bracket (if char in brackets.values()):

If the current character char is one of the open brackets (values in the brackets dictionary), it means an open bracket is encountered.
In this case, the open bracket is pushed onto the stack.
Check if the character is a close bracket (elif char in brackets.keys()):

If the current character char is one of the close brackets (keys in the brackets dictionary), it means a close bracket is encountered.
The code checks if the stack is not empty (if not stack) and if the top of the stack contains the corresponding open bracket.
If the conditions are met, it means a matching pair of brackets is found, and the open bracket is popped from the stack.
Check for Misplaced or Unmatched Brackets (if not stack or stack.pop() != brackets[char]):

If the stack is empty (not stack), or the top of the stack does not contain the expected open bracket for the current close bracket, it indicates a misplacement or unmatched bracket.
In such cases, the function immediately returns False, indicating that the input string is not valid.
    """