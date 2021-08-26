def expressions(nums, current_result=0, current_expression=''):
    if not nums:
        print(f"{current_expression}={current_result}")
        return
    expressions(nums[1:], current_result + nums[0], f"{current_expression}+{nums[0]}")
    expressions(nums[1:], current_result - nums[0], f"{current_expression}-{nums[0]}")


numbers = input().split(', ')
nums = [int(el) for el in numbers]
expressions(nums)

# def expressions(nums, current_sum=0, expression=""):
#     if not nums:
#         return [(expression, current_sum)]
#
#     result_plus = expressions(nums[1:], current_sum+nums[0], f"{expression}+{nums[0]}")
#     result_minus = expressions(nums[1:], current_sum-nums[0], f"{expression}-{nums[0]}")
#     return result_plus + result_minus
#
# numbers = input().split(', ')
# nums = [int(el) for el in numbers]
# print(*[f"{el[0]}={el[1]}" for el in expressions(nums)], sep='\n')
