from math import copysign
class Solution:
    def reverse(self, x: int) -> int:
        s = int(copysign(1, x))
        r = int(str(s*x)[::-1])
        return s*r * (r < 2**31)
    def copysign(x):
        return (x > 0) - (x < 0)

        