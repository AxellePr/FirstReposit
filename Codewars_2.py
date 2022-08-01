numbers = [1, 2, 3, 4, 5]
def sum_two_smallest_numbers(numbers):
    res = sorted(numbers)
    return res[0] + res[1]
print(sum_two_smallest_numbers(numbers))