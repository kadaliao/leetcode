# [122] 买卖股票的最佳时机 II

# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# * algorithms
# * Easy (63.72%)
# * Total Accepted:    233.9K
# * Total Submissions: 367.1K
# * Testcase Example:  '[7,1,5,3,6,4]'

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

#

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。


# 示例 2:

# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。


# 示例 3:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

#

# 提示：


# 	1 <= prices.length <= 3 * 10 ^ 4
# 	0 <= prices[i] <= 10 ^ 4


class Solution(object):
    def maxProfit0(self, prices):
        if not prices:
            return 0
        n = len(prices)

        # 在第n天的某种持有情况下的最大收益
        # 等于
        # 不动（保持现在的持仓）、卖出（新状态无持仓）、买入（新状态🈶️持仓）三种情况的最大收益
        def dfs(index, status):
            if index >= n:
                return 0
            a = dfs(index + 1, status)  # 不动
            b, c = 0, 0
            if status:
                b = dfs(index + 1, 0) + prices[index]  # 卖掉
            else:
                c = dfs(index + 1, 1) - prices[index]  # 买入

            return max(a, b, c)

        return dfs(0, 0)

    # 有状态的dfs
    def maxProfit1(self, prices):
        d = {}
        if not prices:
            return 0
        n = len(prices)
        # cnt = 0

        # 在第n天的某种持有情况下的最大收益
        # 等于
        # 不动（保持现在的持仓）、卖出（新状态无持仓）、买入（新状态🈶️持仓）三种情况的最大收益
        def dfs(index, status):
            if index >= n:
                d[(index, status)] = 0
                return 0

            if (index, status) in d:
                return d[(index, status)]

            a = dfs(index + 1, status)  # 不动
            b, c = 0, 0
            if status:
                b = dfs(index + 1, 0) + prices[index]  # 卖掉
            else:
                c = dfs(index + 1, 1) - prices[index]  # 买入

            res = max(a, b, c)
            d[(index, status)] = res
            # nonlocal cnt
            # cnt += 1
            # print(cnt, (index, status))
            return res

        return dfs(0, 0)

    # 贪心算法
    # 因为买卖没有手续费、可以无限次买卖
    # 所以局部的最优解（吃掉每一次涨幅）可以推导出全局最优解
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            earning = prices[i] - prices[i - 1]
            if earning > 0:
                profit += earning
        return profit


# prices = [7,1,5,3,6,4]
# res = Solution().maxProfit(prices)
# print(res)
