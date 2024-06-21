def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b/gcd(a, b)


a = 10
b = 20
print(lcm(a, b))
