# -*- coding： utf8 -*-
# -----------------------------------------------------------
# leetcode algorithms 1 to 20
# create by jlkang
# -----------------------------------------------------------

import unittest


# no.1 给定一个包含整数的数组，给定一个目标结果，返回数组中两个数相加等
# 于目标结果的索引，假设数组中有唯一的解
def two_sum(nums, target):
    find_num = dict()
    for i, n in enumerate(nums):
        if n not in find_num:
            find_num[target-n] = i
        else:
            return [find_num[n], i]


# no.2 有非空链表代表两个非负整数，每个节点按倒叙存储一位数,计算两个数相
# 加并已链表形式返回
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def travel(l):
    while l is not None:
        print(l.val)
        l = l.next


def add_two_number(l1, l2):
    ret = ListNode(0)
    k = 0
    tmp_ret = ret
    while l1 is not None or l2 is not None or k:
        n1 = n2 = 0
        if l1 is not None:
            n1 = l1.val
            l1 = l1.next
        if l2 is not None:
            n2 = l2.val
            l2 = l2.next
        n = (n1 + n2 +k) % 10
        k = (n1 + n2 + k) // 10
        tmp_ret.next = ListNode(n)
        tmp_ret = tmp_ret.next
    return ret.next


# no.3 找出一个字符串中没有重复元素的最大子串长度
def longest_len_substring_without_repeat(s):
    m = 0
    i = 0
    for j in range(len(s)):
        if s[j] in s[i:j]:
            m = max(m, j-i)
            i += s[i:j].index(s[j]) + 1  
        else:
            m = max(m, j-i+1)
    return m


# no.4 找出两个已经排序的数组的中位数
def find_median_sorted_arrays(l1, l2):
    # todo: too hard
    pass


# no.5 找出字符串中最长的回文子串
def longest_palindrome(s):
    pralind_str = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j] == s[j:i:-1]:
                if j-i+1 > len(pralind_str):
                    pralind_str = s[i:j]
    return pralind_str


# no.40
def combination_sum(candidates, target):
    candidates.sort()
    table = [None] + [set() for _ in range(target)]
    for i in candidates:
        if i > target:
            break
        for j in range(target - i, 0, -1):
            table[i + j] |= {elt + (i,) for elt in table[j]}
        table[i].add((i,))
    return map(list, table[target])


# no.42
class Stack(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = [None] * self._capacity
        self._top = -1

    def push(self, value):
        self._top += 1
        self._stack[self._top] = value

    def pop(self):
        value = self._stack[self._top]
        self._top -= 1
        return value

    @property
    def top(self):
        return self._stack[self._top]

    def is_empty(self):
        if self._top < 0:
            return True
        return False


def trap_rain_water(nums):
    water = 0
    stack = Stack(len(nums))
    for i, n in enumerate(nums):
        if n <= 0:
            continue
        if stack.is_empty():
            stack.push((i, n))
            continue
        if n >= stack.top[1] and i - stack.top[0] > 1:
            _i, _n = stack.pop()
            pool = (i - _i -1) * min(_n, n)
            block = 0
            for _ in range(_i + 1, i):
                block += nums[_]
            water += pool - block
            stack.push((i, n))
        elif n >= stack.top[1] and i - stack.top[0] == 1:
            stack.pop()
            stack.push((i, n))
        else:
            pass
    return water

if __name__ == '__main__':
    s = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_rain_water(s))