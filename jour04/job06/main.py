L = list(range(0, 21))

def echange():
    L[0], L[20] = L[20],L[0]
    return L

print(echange())
