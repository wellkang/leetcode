# -*- coding: utf-8 -*-

"""
"""


def combination_sum4(nums, target):
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for i in range(target + 1):
        if dp[i] == 0:
            continue
        for n in nums:
            if i + n <= target:
                dp[i+n] += dp[i]
    return dp[-1]


if __name__ == '__main__':
    print(combination_sum4([5, 7], 12))
