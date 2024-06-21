num = int(input("Enter the number"))
for i in range(0, num-1):
    for j in range(i+1, 0, -1):
        print(j, end=" ")
    print()
