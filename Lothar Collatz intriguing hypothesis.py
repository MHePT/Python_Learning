c0 = int(input("Enter Number:"))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = c0 * 3 + 1
    print(c0)
    steps +=1
print("Steps= ",steps)