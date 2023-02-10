def ways_to_climb(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return ways_to_climb(n - 1) + ways_to_climb(n - 2)
