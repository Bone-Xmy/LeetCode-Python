class Solution:
    # ********动态规划（dp）***********
    def longestCommonSubsequence(self, text1, text2):
        if not text1 or not text2:
            return 0
        m = len(text1)
        n = len(text2)
        # 初始化数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        print(dp)
        t = [0,0] * 5
        print(t)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果最后一个字符相同，则dp方程如下
                    # 此处应该将每次循环遍历的text部分当做一个整体，当i == m + 1,j == n + 1 的时候等于完整的text

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1] # 最后一个字符相同，则公共部分加 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # 如果最后一个字符不相同，则取text1去掉最后一个字符或者text2去掉最后一个字符的最大公共子序列

            return dp[m][n]

if __name__ == "__main__":
    s = Solution()
    s.longestCommonSubsequence("abcde", "caef")        
