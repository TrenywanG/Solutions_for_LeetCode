#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    :   001_two_sum.py
@Time    :   2020/08/22 16:35
@Author  :   TrenywanG
@Version :   1.0
@Contact :   brtxbrc0521@126.com
"""


# here put the import lib

class Solution:
    def twosum(self, nums, target):
        output = []
        for i, num_i in enumerate(nums):
            if target - num_i in nums and i != nums.index(target - num_i):
                output.extend((i, nums.index(target - num_i)))
            return output


if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.twosum([2, 7, 11, 15], 9))
