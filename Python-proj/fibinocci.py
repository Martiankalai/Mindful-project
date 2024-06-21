nterms = int(input("Enter a number of terms"))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Enter a positive number")
elif nterms == 1:
    print("Fibinocci Series", n1)
else:
    print("Fiboncci Series")
    while (count < nterms):
        print(n1, end=" ")
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1
