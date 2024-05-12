from typing import List

class Solution:
    def nCr(self, n: int, r: int) -> int:
        res = 1

        # calculating nCr:
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)

        return res

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [self.nCr(i, j) for j in range(i + 1)]
            triangle.append(row)

        return triangle