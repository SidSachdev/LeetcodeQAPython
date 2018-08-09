class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = []
        # constructs a grid
        for i in range(m):
            path.append([None for i in range(n)])

        # populates grid by column starting from top-left
        for col in range(m):
            for row in range(n):
                # first square should be 1 since there's only 1 path
                if row == 0 and col == 0:
                    path[col][row] = 1
                    continue
                sum = 0
                # there's a path from left square
                if row != 0:
                    sum += path[col][row - 1]
                # there's a path from top square
                if col != 0:
                    sum += path[col - 1][row]
                path[col][row] = sum

        return path[-1][-1]






class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        memo, m, n = {}, len(obstacleGrid), len(obstacleGrid[0])

        def helper(i, j):
            if (i, j) in memo:
                return memo[i, j]
            ans = 0
            if not obstacleGrid[i-1][j-1]:
                if i < m:
                    ans += helper(i+1, j)
                if j < n:
                    ans += helper(i, j+1)
                if i == m and j == n:
                    ans += 1
            memo[i, j] = ans
            return memo[i, j]

        return helper(1, 1)