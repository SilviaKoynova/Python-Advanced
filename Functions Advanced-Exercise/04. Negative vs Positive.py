nums = list(map(int, input().split()))
negative = [i for i in nums if i < 0]
negative_sum = (sum(negative))
print(negative_sum)
positive = [i for i in nums if i >= 0]
positive_sum = (sum(positive))
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")



# def print_stronger_nums(nums):
#     positive_sum = sum(filter(lambda x: x > 0, nums))
#     negative_sum = sum(filter(lambda x: x < 0, nums))
#     print(negative_sum, positive_sum, sep="\n")
#     if positive_sum > abs(negative_sum):
#         print(f"The positives are stronger than the negatives")
#     else:
#         print("The negatives are stronger than the positives")
#
#
# numbers = list(map(int, input().split()))
# print_stronger_nums(numbers)
