class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
        1: "I",   5: "V",    4: "IV",
        10: "X",  9: "IX",
        50: "L",  40: "XL",
        100: "C", 90: "XC",
        500: "D", 400: "CD",
        1000: "M", 900: "CM",
    }
    
        r=''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
    # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num -= n

        return r
    
    """
    Now, let's go through the code with num = 19:

Initial Setup:

num is initially set to 19.
r is an empty string.
First Iteration (n=10):

The loop checks if 10 <= 19. It is true.
It appends the corresponding Roman numeral representation (num_map[10], which is "X") to r.
It subtracts 10 from num, making num = 9.
Second Iteration (n=9):

The loop checks if 9 <= 9. It is true.
It appends the corresponding Roman numeral representation (num_map[9], which is "IX") to r.
It subtracts 9 from num, making num = 0.
Loop Ends:

The loop ends because 9 is no longer less than or equal to num.
Result:

The final result is the string r, which is "XIX".
    """