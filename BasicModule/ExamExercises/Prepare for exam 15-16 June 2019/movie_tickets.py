a1 = int(input())
a2 = int(input())
n = int(input())

for symbol_1 in range(a1, a2):
    for symbol_2 in range(1, n + 1):
        for symbol_3 in range(1, n // 2 + 1):
            symbol_4 = ord(chr(symbol_1))
            if symbol_1 % 2 != 0 and (symbol_2 + symbol_3 + symbol_4) % 2 != 0:
                print(f"{chr(symbol_1)}-{symbol_2}{symbol_3}{chr(symbol_4)}")
