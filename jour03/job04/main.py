def compteur(str):
    i=0
    while i < str:
        i = i + 1
        if i %3 ==0 and i %5==0:
            print ("fizzbuzz")
        elif i %3 ==0:
            print("fizz")
        elif i %5 ==0:
            print("buzz")
        else:
            print(i)




compteur(100)