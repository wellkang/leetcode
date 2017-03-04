from functools import reduce


def reverse(n):
    numbers = []
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n:
        numbers.append(n % 10)
        n //= 10
    result = 0
    for i in range(len(numbers)):
        result += numbers[i] * 10 ** (len(numbers) - i - 1)
    return sign * result


if __name__ == '__main__':
    print(reverse(-91993994))
