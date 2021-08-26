# text = input().split()
# result = [word for word in text if len(word) % 2 == 0]
# for w in result:
#     w = str(w)
#     print(w)
text = input().split()
result = [str(word) for word in text if len(word) % 2 == 0]
print('\n'.join(str(word) for word in result))