# -*- coding: utf-8 -*-

"""
"""


def wiggle_max_length(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums:
        find = False
        k = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if find is False:
                k += 1
                flag = nums[i] - nums[i-1]
                find = True
            elif find is True:
                if (nums[i] - nums[i-1])*flag < 0:
                    k += 1
                    flag = -1 * flag
    else:
        k = 0
    return k

if __name__ == '__main__':
    print(wiggle_max_length([1,7,4,9,2,5]))
