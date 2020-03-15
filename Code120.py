class Solution:
    def minimumTotal(self, triangle):
        dp = triangle

        # eg：一个3层高的三角形，则从 1 开始，到 -1 结束（不包括 -1），每次减少 1
        # 依次取值：1，0
        # 当 i = 1 的时候，i + 1 正好判断的是最后一层的数据
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # 正下方与对角线中的较小者即为最短路径
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        print(triangle[0][0])
        return dp[0][0] # 三角形最上面的记录

    # 0(n*n/2) space, top-down
    # xrange 与 range 用法与完全相同，所不同的是xrange生成的不是一个数组，而是一个生成器
    # xrang 做循环的性能比range好，尤其是返回很大的时候，尽量用xrange吧，除非你是要返回一个列表
    def minimumTotal1(self, triangle):
        if not triangle:
            return
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        # for i in xrange()





        