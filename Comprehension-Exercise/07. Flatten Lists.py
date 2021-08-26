# data = input().split("|")
# data.reverse()
#
# result = []
# for iteration in range(len(data)):
#     for value in data[iteration].split():
#         result.append(value)
#
# print(*result)
# sequences = input().split('|')
# numbers = []
# for seq in sequences:
#     row = []
#     for element in seq.split(' '):
#         if element.isnumeric():
#             row.append(int(element))
#     numbers.append(row)
sequences = input().split('|')
numbers = [[int(element) for element in seq.split() if element.isdigit()] for seq in sequences]
numbers.reverse()
numbers = [number for sequence in numbers for number in sequence]
print(*numbers)
