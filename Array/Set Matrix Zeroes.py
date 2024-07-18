class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(mat)
        n = len(mat[0])
        rows = [0 for i in range(m)]
        cols = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    mat[i][j] = 0