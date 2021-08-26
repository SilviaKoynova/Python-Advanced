# nums = [abs(float(el))for el in input().split()]
# print(nums)
def absolute_numbers(seq):
    return [abs(el) for el in seq]


nums = [float(el) for el in input().split()]
print(absolute_numbers(nums))