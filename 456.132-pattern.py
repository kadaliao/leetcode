#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#
# https://leetcode-cn.com/problems/132-pattern/description/
#
# algorithms
# Medium (29.62%)
# Total Accepted:    28.8K
# Total Submissions: 88.4K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k]
# 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
#
# 如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
#
#
#
# 进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。
#
#
# 示例 2：
#
#
# 输入：nums = [3,1,4,2]
# 输出：true
# 解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
#
#
# 示例 3：
#
#
# 输入：nums = [-1,3,2,0]
# 输出：true
# 解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1
# -10^9
#
#
#

from typing import List


class Solution:
    def find132pattern0(self, nums: List[int]) -> bool:
        n = len(nums)
        numsi = nums[0]
        for j in range(1, n):
            for k in range(n - 1, j, -1):
                if numsi < nums[k] < nums[j]:
                    return True
            numsi = min(numsi, nums[j])
        return False

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        left_min = [float("inf")] * n
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i - 1])
        stack = []
        for j in range(n - 1, -1, -1):
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]:
                numsk = stack.pop()
            if left_min[j] < numsk:
                return True
            stack.append(nums[j])
        return False
