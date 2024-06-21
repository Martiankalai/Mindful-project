def palin(str):
    reverse = str[::-1]
    return reverse


str = input("Enter a string")
print(palin(str))
word = str
if palin(str) == str:
    print("Palindrome")
else:
    print("Not a Palindrome")
