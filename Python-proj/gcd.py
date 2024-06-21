# Python code to demonstrate naive
# method to compute gcd ( recursion )

def hcfnaive(a, b):
    if (b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)


a = 30
b = 10

# prints 12
print("The gcd is : ", end="")
print(hcfnaive(a, b))
