def sum_of_natural_numbers(start, end):
    if start > end:
        return 0
    return start + sum_of_natural_numbers(start + 1, end)

print(sum_of_natural_numbers(1, 10))
