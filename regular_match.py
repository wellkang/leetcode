import unittest


def is_match(s, p):
    dp_table = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
    dp_table[0][0] = True
    for i in range(2, len(p)+1):
        if p[i-1][0] == '*':
            dp_table[i][0] = dp_table[i-2][0]
    for i in range(1, len(p)+1):
        for j in range(1, len(s)+1):
            if p[i-1] != '*':
                dp_table[i][j] = dp_table[i-1][j-1] and (p[i-1]==s[j-1] or p[i-1]=='.')
            else:
                dp_table[i][j] = dp_table[i-2][j] or dp_table[i-1][j]
                # print('i----j::', i, j)
                # print(dp_table[i-2][j], dp_table[i-1][j])
                # print(dp_table)
                if p[i-2] == s[j-1] or p[i-2] == '.':
                    dp_table[i][j] |= dp_table[i][j-1]
    return dp_table[-1][-1]


class TestSolution(unittest.TestCase):

    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(is_match(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(is_match(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(is_match(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(is_match(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(is_match(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(is_match(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(is_match(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(is_match(s, p))


if __name__ == "__main__":
    unittest.main()
