memdict = {0: 1, 1: 1}


def fibonnci(n):
    if n in memdict:
        return memdict[n]
    else:
        result = fibonnci(n-1)+fibonnci(n-2)
        memdict[n] = result
        return result


n = int(input("Fibonnci number:"))
print(fibonnci(n))
