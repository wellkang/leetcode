def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    point = (0, 0)
    for i in range(n):
        if i < n - 1 and s[i] == s[i + 1]:
            point = (i, i + 1) if point[1] - point[0] < 1 else point
        for j in range(1, min(1 + i, n - i)):
            if s[i] == s[i + 1]:
                point = (i, i + 1) if point[1] - point[0] < 1 else point
                try:
                    if s[i - j] == s[i + 1 + j]:
                        point = (i - j, i + 1 + j) if point[1] - point[0] < (j + 1) * 2 else point
                    else:
                        break
                except IndexError:
                    pass
        for j in range(1, min(1 + i, n - i)):
            if s[i - j] == s[i + j]:
                point = (i - j, i + j) if point[1] - point[0] < 2 * j + 1 else point
            else:
                break

    return s[point[0]:point[1] + 1]


def longestPalindrome1(self, s):
    if len(s) == 0:
        return 0
    maxLen = 1
    start = 0
    for i in range(len(s)):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            start = i - maxLen - 1
            maxLen += 2
            continue

        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            start = i - maxLen
            maxLen += 1
    return s[start:start + maxLen]