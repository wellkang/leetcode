# -----------------------------------------------------------
# leetcode algorithms 1 to 20
# create by jlkang
# -----------------------------------------------------------

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


if __name__ == '__main__':
    s = 'pwwkew'
    print(longest_len_substring_without_repeat(s))