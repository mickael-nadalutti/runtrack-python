def compteur(str):
    i = 0
    while i < str:
        if i == 26:
            i +=1
        elif i == 37:
            i +=1
        elif i == 88:
            i +=1
        print(i)
        i = i + 1

compteur(101)
