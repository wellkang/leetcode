def is_palindrome(x):
    tmp_x = x
    nums = []
    while tmp_x > 0:
        nums.append(tmp_x % 10)
        tmp_x //= 10
    y = 0
    for n in nums:
        y = y * 10 + n
    return x == y


if __name__ == '__main__':
    print(is_palindrome(11211))
