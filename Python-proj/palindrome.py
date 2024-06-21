string = input("Enter the string:")
reverse = string[::-1]
print(reverse)
if string == reverse:
    print("It is a palindrome")
else:
    print("It is not a  palindrome")
