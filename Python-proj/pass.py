import re
password = input("Enter")
flag = 0
while (True):
    if (len(password) < 8):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    else:
        flag = 0
        print("Not valid")
        break
if flag == -1:
    print("Valid")
