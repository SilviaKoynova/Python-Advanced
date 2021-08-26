def odd(nums):
    odd_sum = sum(filter(lambda x: x % 2 != 0, nums))
    return odd_sum * len(nums)


def even(nums):
    even_sum = sum(filter(lambda x: x % 2 == 0, nums))
    return even_sum * len(nums)


command = input()
numbers = [int(i) for i in input().split()]

if command == 'Odd':
    print(odd(numbers))
elif command == 'Even':
    print(even(numbers))
