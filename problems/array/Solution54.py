"""   Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
   
   [
   [1, 1, 1, 1, 1, 1, 1], <- top layer    1, 1, 1, 1, 1, 1, 1
   [1, 2, 2, 2, 2, 2, 1], 
   [1, 2, 3, 3, 3, 2, 1],
   [1, 2, 2, 2, 2, 2, 1], 
   [1, 1, 1, 1, 1, 1, 1]  <- bottom layer    1, 1, 1, 1, 1
   ]
"""


class Solution54:

    def spiralOrder(self, matrix):
        ans = []
        if not matrix:
            return ans
        rows, cols = len(matrix), len(matrix[0])
        r1 = 0
        r2 = rows - 1
        c1 = 0
        c2 = cols - 1

        while r1 <= r2 and c1 <= c2:
            # top layer
            for c in range(c1, c2 + 1):
                ans.append(matrix[r1][c])
            # right side
            for r in range(r1 + 1, r2 + 1):
                ans.append(matrix[r][c2])

            if r1 < r2 and c1 < c2:  # to avoid duplicates
                # bottom layer
                for c in range(c2 - 1, c1, -1): # NOTE: the last index in range is not included !!
                    ans.append(matrix[r2][c])
                # left side
                for r in range(r2, r1, -1):
                    ans.append(matrix[r][c1])

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return ans
