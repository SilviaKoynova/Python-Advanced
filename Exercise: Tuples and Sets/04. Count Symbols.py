text = input()
symbols = {}
for ch in text:
    symbols[ch] = text.count(ch)
sorted_data = sorted(symbols.items(), key=lambda x: x[0])
for el in sorted_data:
    print(f"{el[0]}: {el[1]} time/s")