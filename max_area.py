def max_area(height):
    i = 0
    j = len(height) - 1
    water = 0
    while i < j:
        high = min(height[i], height[j])
        water = max(water, high * (j - i))
        while height[i] <= high and i < j:
            i += 1
        while height[j] <= high and i < j:
            j -= 1
    return water


if __name__ == '__main__':
    max_area([1,1])