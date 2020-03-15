from collections import defaultdict

class Solution:
    def unionPaths(self, m, n):
        def one():
            return 1
        ways = [defaultdict(one) for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[m - 1][n - 1]

    def unionPaths_2(self, m, n):
        def one():
            return 1
        ways = [1 for i in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j - 1]

        return ways[n - 1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.unionPaths_2(3,2))
