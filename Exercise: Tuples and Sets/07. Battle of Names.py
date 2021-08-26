n = int(input())
even_num_set = set()
odd_num_set = set()
for current_iteration_count in range(1, n+1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // current_iteration_count
    if current_sum % 2 == 0:
        even_num_set.add(current_sum)
    else:
        odd_num_set.add(current_sum)
sum_even = sum(even_num_set)
sum_odd = sum(odd_num_set)
if sum_even == sum_odd:
    modified_set = [str(el) for el in even_num_set.union(odd_num_set)]
    print(f"{', '.join(modified_set)}")
elif sum_odd > sum_even:
    modified_set = [str(el) for el in odd_num_set.difference(even_num_set)]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [str(el) for el in even_num_set.symmetric_difference(odd_num_set)]
    print(f"{', '.join(modified_set)}")
