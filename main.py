square = input("Enter a Square (like a1, b2,....): ")

col = ord(square[0]) - ord("a")
row = int(square[1]) - 1

if (col + row) % 2 == 0:
    print("Black square")
else:
    print("White square")    